import time
import uuid
import json
import requests

from src.shared.infrastructure.alexa_skills.get_access_token import get_access_token
from src.shared.infrastructure.environments.variables import utc_format, alexa_proactive_events_uri


def send_proactive_message(creator, message):
    scope = 'proactive_events'
    headers = {
        "Authorization": "Bearer {}".format(get_access_token(scope=scope)),
        "Content-Type": "application/json;charset=UTF-8"
    }

    seconds = time.time()
    timestamp = time.strftime(utc_format(), time.gmtime(seconds))
    reference_id = str(uuid.uuid4())
    seconds += 86400
    expiry_time = time.strftime(utc_format(), time.gmtime(seconds))

    m = f"{creator.lower()}, {message.lower()}"

    params = {
        "timestamp": timestamp,
        "referenceId": reference_id,
        "expiryTime": expiry_time,
        "event": {
            "name": "AMAZON.MessageAlert.Activated",
            "payload": {
                "state": {
                    "status": "UNREAD",
                    "freshness": "NEW"
                },
                "messageGroup": {
                    "creator": {
                        "name": m
                    },
                    "count": 1,
                }
            }
        },
        "relevantAudience": {
            "type": "Multicast",
            "payload": {}
        }
    }

    response = requests.post(alexa_proactive_events_uri(), headers=headers, data=json.dumps(params),
                             allow_redirects=True)
    return response.status_code
