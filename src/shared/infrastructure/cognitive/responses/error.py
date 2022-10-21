import random


def get_error_message(user):
    words = []

    words.append(
        "No entendí " + user + "\n¿Podrías ser más específico por favor?\nTambién pudes pedir /ayuda sobre algo que quieras realizar")

    return random.choice(words)
