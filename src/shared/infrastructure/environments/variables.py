from dotenv import load_dotenv
import os

load_dotenv()


def wifi_ssid():
    return os.environ.get("wifi_sid")


def wifi_password():
    return os.environ.get("wifi_password")


def telegram_token_value():
    return os.environ.get("telegram_token")


def db_url_value():
    return os.environ.get("db_url")


def alexa_client():
    return os.environ.get("alexa_client")


def alexa_secret():
    return os.environ.get("alexa_secret")


def utc_format():
    return "%Y-%m-%dT%H:%M:%S.00Z"


def alexa_token_uri():
    return os.environ.get("alexa_token_uri")


def alexa_proactive_events_uri():
    return os.environ.get("alexa_proactive_events_uri")
