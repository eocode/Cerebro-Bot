import random

from src.shared.infrastructure.cognitive.responses.context import get_hour

HELPERS = ['ayuda', 'help', 'uso', 'usar']


def get_help(user):
    words = []

    hour = get_hour()

    if 0 <= hour < 5:
        words.append("Me agarraste durmiendo " + user + ",\nAcá te muestro algunas opciones:")
        words.append("Sin importar la hora estoy aquí para ayudarte " + user + "\nRevisa las siguientes opciones:")

    if 5 <= hour < 12:
        words.append("Estoy aquí para ayudarte desde temprano " + user + "\nRevisa las siguientes opciones:")

    if 12 <= hour < 19:
        words.append("Espero que te encuentres bien " + user + "\nRevisa las siguientes opciones:")
        words.append("Estoy aquí para lo que necesites " + user + "\nRevisa las siguientes opciones:")
        words.append("Un gusto ayudarte " + user + "\nRevisa las siguientes opciones:")

    if 19 <= hour < 22:
        words.append("Se acerca el final del día " + user + "Alguna de estás opciones te puede ayudar:")

    if 22 <= hour <= 24:
        words.append("Es hora de dormir " + user + "\n¿Qué necesitas?")

    return random.choice(words)
