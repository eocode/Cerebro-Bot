import random

WIFI = ['wifi', 'internet']


def get_wifi(user):
    words = []

    words.append("Claro " + user + "\nLos datos para conectarse a la red son los siguientes:")

    return random.choice(words)
