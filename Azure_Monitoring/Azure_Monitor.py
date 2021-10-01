#!/usr/bin/env python3
import time
import requests
import json
import datetime
import automationassets
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.compute import ComputeManagementClient
from .SendSlack import SendSlack

def get_resources_in_group(resource_client, resource_group, resource_type=None):
    items = []
    for item in resource_client.resources.list_by_resource_group(resource_group):
        if resource_type == "vm":
            if item.type == "Microsoft.Compute/virtualMachines":
                items.append(item)
        elif resource_type == "storage":
            if item.type == "Microsoft.Storage/storageAccounts":
                items.append(item)
        elif resource_type == "disk":
            if item.type == "Microsoft.Compute/disks":
                items.append(item)
        elif not resource_type:
            items.append(item)
        else:
            raise Exception("Unknown type")
    return items


def get_vm_sizes(compute_client, region, vm_name, vm_sizetype):
    vm_sizes_list = compute_client.virtual_machine_sizes.list(location=region)
    for vm_size in vm_sizes_list:
        if vm_size.name == vm_sizetype:
            return vm_size.memory_in_mb


def get_usage_from_day(monitor_client, vm_id, group_name, group_location, vm_name, vm_type, type="cpu"):
    start = datetime.datetime.now() - datetime.timedelta(minutes=10)
    stop = datetime.datetime.now()
    assert type in ['cpu', 'memory']
    metric = "Percentage CPU" if type == 'cpu' else 'Available Memory Bytes'
    metrics_data = monitor_client.metrics.list(
        vm_id,
        timespan="{}/{}".format(start, stop),
        interval='PT5M',
        metricnames=metric,
        aggregation='Average'
    )
    usage = []
    for item in metrics_data.value:
        print("{} ({})".format(item.name.localized_value, item.unit.name))
        # azure.mgmt.monitor.models.Metric
        for timeserie in item.timeseries:
            for data in timeserie.data:
                print("{}: {}".format(data.time_stamp, data.average))
                usage.append(data.average)
    return usage


def alter_level(value):
    if value >= 90:
        return "critical"
    elif value >= 70 and value < 90:
        return "danger"
    elif value >= 50 and value < 70:
        return "warning"
    else:
        return "good"


def trackdown_vms_in_rg(resource_group, resource_client, compute_client, monitor_client):
    items = get_resources_in_group(resource_client, resource_group, resource_type="vm")
    # disk_items = get_resources_in_group(resource_client, resource_group, resource_type="disk")

    print("=====================================================================")

    for item in items:
        vm_detail = compute_client.virtual_machines.get(resource_group, item.name, expand='instanceView')
        if vm_detail.instance_view.statuses[1].code == 'PowerState/running':
            print(item.name, vm_detail.instance_view.statuses[1].code)
            per_cpu, aft_cpu = get_usage_from_day(monitor_client, item.id, group.name, item.location, item.name,
                                                  item.type, type="cpu")
            before = alter_level(per_cpu)
            current = alter_level(aft_cpu)
            print(per_cpu, aft_cpu)
            print(before, current)

            # current value
            cpu_alter_type = "CPU"
            if current == "critical":
                SendSlack.message(current, aft_cpu, group.name, item.location, item.name, cpu_alter_type)
            elif current == "danger":
                SendSlack.message(current, aft_cpu, group.name, item.location, item.name, cpu_alter_type)
            elif current == "warning":
                SendSlack.message(current, aft_cpu, group.name, item.location, item.name, cpu_alter_type)
            elif before == "critical" and current == "good":
                SendSlack.message(current, aft_cpu, group.name, item.location, item.name, cpu_alter_type)
            elif before == "danger" and current == "good":
                SendSlack.message(current, aft_cpu, group.name, item.location, item.name, cpu_alter_type)
            else:
                print("Except")

            # total mem
            vm = compute_client.virtual_machines.get(group.name, item.name)
            total_mem = get_vm_sizes(compute_client, item.location, item.name, vm.hardware_profile.vm_size)
            total_mem = total_mem * 1048576

            mem1, mem2 = get_usage_from_day(monitor_client, item.id, group.name, item.location, item.name, item.type,
                                            type="memory")

            mem1_1 = (total_mem - mem1) / total_mem
            mem1_1 = mem1_1 * 100

            mem2_2 = (total_mem - mem2) / total_mem
            mem2_2 = mem2_2 * 100

            before_mem = alter_level(mem1_1)
            current_mem = alter_level(mem2_2)

            print(mem1_1, mem2_2)
            print(before_mem, current_mem)

            mem_alter_type = "Memory"
            if current_mem == "critical":
                SendSlack.message(current_mem, mem2_2, group.name, item.location, item.name, mem_alter_type)
            elif current_mem == "danger":
                SendSlack.message(current_mem, mem2_2, group.name, item.location, item.name, mem_alter_type)
            elif current_mem == "warning":
                SendSlack.message(current_mem, mem2_2, group.name, item.location, item.name, mem_alter_type)
            elif before_mem == "critical" and current_mem == "good":
                SendSlack.message(current_mem, mem2_2, group.name, item.location, item.name, mem_alter_type)
            elif before_mem == "danger" and current_mem == "good":
                SendSlack.message(current_mem, mem2_2, group.name, item.location, item.name, mem_alter_type)
            else:
                print("Except")

        else:
            print(item.name, vm_detail.instance_view.statuses[1].code)
            SendSlack.message_text(group.name, item.name)


def get_automation_runas_credential(runas_connection):
    from OpenSSL import crypto
    import binascii
    from msrestazure import azure_active_directory
    import adal

    # Get the Azure Automation RunAs service principal certificate
    cert = automationassets.get_automation_certificate("AzureRunAsCertificate")
    pks12_cert = crypto.load_pkcs12(cert)
    pem_pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pks12_cert.get_privatekey())

    # Get run as connection information for the Azure Automation service principal
    application_id = runas_connection["ApplicationId"]
    thumbprint = runas_connection["CertificateThumbprint"]
    tenant_id = runas_connection["TenantId"]

    # Authenticate with service principal certificate
    resource = "https://management.core.windows.net/"
    authority_url = ("https://login.microsoftonline.com/" + tenant_id)
    context = adal.AuthenticationContext(authority_url)
    return azure_active_directory.AdalAuthentication(
        lambda: context.acquire_token_with_client_certificate(
            resource,
            application_id,
            pem_pkey,
            thumbprint)
    )


if __name__ == '__main__':
    subscription_id = 'xxxxx'
    tenant_id = 'xxxxx'

    runas_connection = automationassets.get_automation_connection("AzureRunAsConnection")
    credentials = get_automation_runas_credential(runas_connection)

    # create client
    computeclient = ComputeManagementClient(credentials, subscription_id)
    monitorclient = MonitorManagementClient(credentials, subscription_id)
    resourceclient = ResourceManagementClient(credentials, subscription_id)

    # Get list of resource groups in the subscription
    groups = []
    groups = resourceclient.resource_groups.list()
    for group in groups:
        print('Resource group: ' + group.name + ' Location: ' + group.location)
        trackdown_vms_in_rg(group.name, resourceclient, computeclient, monitorclient)
