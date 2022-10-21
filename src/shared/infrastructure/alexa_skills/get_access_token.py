import json
import requests

from src.shared.infrastructure.environments.variables import alexa_client, alexa_secret, alexa_token_uri


def get_access_token(scope):

    client = alexa_client()
    secret = alexa_secret()
    uri = alexa_token_uri()

    token_params = {
        "grant_type": "client_credentials",
        "scope": f"alexa::{scope}",
        "client_id": client,
        "client_secret": secret
    }

    print(token_params)

    token_headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }

    response = requests.post(uri, headers=token_headers, data=json.dumps(token_params),
                             allow_redirects=True)

    print("Token response status: " + format(response.status_code))
    print("Token response body  : " + format(response.text))

    if response.status_code != 200:
        print("Error calling LWA!")
        return None

    access_token = json.loads(response.text)["access_token"]
    return access_token
