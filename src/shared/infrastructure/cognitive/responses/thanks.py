import random

from src.shared.infrastructure.cognitive.responses.context import get_hour

THANKS = ['gracias', 'agradezco']


def get_thanks(user):
    words = []

    hour = get_hour()

    if 0 <= hour < 5:
        words.append("Un gusto ayudarte" + user + "\nDescansa")

    if 5 <= hour < 12:
        words.append("Estoy aquí para ayudarte " + user + "\nQué tengas buen día")
        words.append("Estoy aquí para ayudarte " + user + "\nQué tengas un excelente día")
        words.append("No hay de que " + user + "\nQué tengas un excelente día")
        words.append("No hay de que " + user + "\nQué tengas buen día")
        words.append("Estoy aquí para lo que necesites " + user + "\nQué tengas buen día")

    if 12 <= hour < 19:
        words.append("No hay de que " + user + "\nQué tengas buena tarde")
        words.append("Estoy aquí para lo que necesites " + user + "\nBuena tarde")
        words.append("No hay de que " + user + "\nBuen día")

    if 19 <= hour < 22:
        words.append("Para lo que necesites " + user + "\nQué tengas buenas noche")
        words.append("Cualquier cosa aquí ando " + user + "\nBuen as noches")

    if 22 <= hour <= 24:
        words.append("No hay de que " + user + "\nDescansa")

    return random.choice(words)
