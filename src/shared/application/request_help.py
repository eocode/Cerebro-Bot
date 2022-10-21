from src.shared.infrastructure.cognitive.responses.account import get_unnaccess
from src.user.application.use_case.get_account import GetAccount


def request_help(user):
    usr, access, info = GetAccount().execute(permission='settings', chat_id=user.id,
                                             name=user.first_name, username=user.username)
    response = []
    if access:
        response.append(
            f"/cuenta Acerca de tu cuenta\n/pago Tú próximo pago\n/wifi Clave de "
            f"internet\n/dispositivos Registra tus dispositivos\n/problemas Reporta un problema\n/garrafones Compra "
            f"garrafones de "
            f"agua")
    else:
        return get_unnaccess()

    return response
