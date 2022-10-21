import random

from src.shared.infrastructure.cognitive.responses.context import get_hour

GREETINGS = ['hola', 'hi', 'hello', 'que onda', 'quiubo']


def get_greeting(user):
    words = []

    hour = get_hour()

    if 0 <= hour < 5:
        words.append("¡Hola " + user + ", deberías de estár durmiendo a estas horas!")

    if 5 <= hour < 12:
        words.append("¡Hola " + user + ", que tengas un buen día!")
        words.append("Buenos días " + user)
        words.append("Hola " + user + ', buen día')
        words.append("Hola, buen día " + user)

    if 12 <= hour < 19:
        words.append("Hola " + user)
        words.append("Buenas tardes " + user)
        words.append("Qué tal " + user)

    if 19 <= hour < 22:
        words.append("Buenas noches " + user)
        words.append("Hola " + user + ", buenas noches")
        words.append("Hola " + user + ", espero hayas tenido un gran día")

    if 22 <= hour <= 24:
        words.append("Hola, ya casi es hora de ir a dormir " + user + ', descansa')
        words.append("Hola " + user + ' ¿qué haces en el teléfono a estas horas?, ya estaba dormido, buenas noches')

    return random.choice(words)
