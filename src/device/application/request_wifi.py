from src.shared.application.query import call_sql
from src.shared.infrastructure.environments.variables import wifi_ssid, wifi_password
from src.user.application import module_wifi
from src.user.application.use_case.get_account import GetAccount


def request_wifi(user):
    usr, access, info = GetAccount().execute(permission='wifi', chat_id=user.id,
                                             name=user.first_name, username=user.username)

    call_sql(action="Wifi request", module=module_wifi, chat_id=user.id, type='user')

    response = []

    if access:
        response.append(f"SSID: {wifi_ssid()}\nPassword: {wifi_password()}")
        response.append("Detalles de la red:\n40m² de alcance\n500mb Bajada\n50 mb Subida")
        response.append(
            "Recuerda: Una vez ingreses con tus dispositivos, tendrás 24hrs para registrarlos en /dispositivos")
        response.append("Si no los registras serán bloqueados y perderás el acceso a la red aún ingresando la clave")
        response.append("Disfruta de tú conexión :D")
    else:
        response.append("Lo sentimos no tienes acceso al wifi")

    return response
