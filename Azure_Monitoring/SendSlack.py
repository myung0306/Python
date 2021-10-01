import requests
import json

def message(status, val, groupname, grouplocation, vmname, alter_type):
    status_code = {"critical": "치명", "danger": "위험", "warning": "주의", "good": "안전"}
    status_text = {"critical": vmname + " is Critical at " + grouplocation,
                   "danger": vmname + " is Danger at " + grouplocation,
                   "warning": vmname + " is Warning at " + grouplocation, "good": vmname + " is OK at " + grouplocation}

    slack_data = {
        "username": "AlertSite",
        "icon_url": "https://smartbear.com/SmartBear/media/images/icons/AlertSite-icon.png",
        "text": ":loudspeaker: Azure 모니터링 알림-" + alter_type + "\n" + status_text[status],
        "attachments": [
            {
                "color": status,
                "fields": [
                    {
                        "title": "Current Status",
                        "value": str(status) + '-' + str(val) + '%'
                    },
                    {
                        "title": "Resource Group",
                        "value": groupname
                    },
                    {
                        "title": "Name",
                        "value": vmname,
                    }
                ]
            }
        ]
    }

    webhook_url = 'xxxxx'

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}, verify=False
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


def message_text(groupname, vmname):
    slack_data = {
        "username": "AlertSite",
        "icon_url": "https://smartbear.com/SmartBear/media/images/icons/AlertSite-icon.png",
        "text": ":loudspeaker: Azure 모니터링 알림 - Server Down\n",
        "attachments": [
            {
                "color": "danger",
                "fields": [
                    {
                        "title": "Resource Group",
                        "value": groupname
                    },
                    {
                        "title": "Name",
                        "value": vmname,
                    }
                ]
            }
        ]
    }

    webhook_url = 'xxxxx'

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}, verify=False
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )