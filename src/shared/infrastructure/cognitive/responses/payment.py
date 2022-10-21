import random

PAYMENTS = ['pago', 'pagos', 'facturas', 'debo', 'pagar', 'cuanto']


def get_payment(user):
    words = []

    words.append("Un momento " + user + "\nEstoy consultando tus datos de pago:")

    return random.choice(words)
