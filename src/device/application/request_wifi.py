from src.shared.application.query import call_sql
from src.shared.infrastructure.cognitive.responses.account import get_unnaccess
from src.shared.infrastructure.environments.variables import wifi_ssid, wifi_password
from src.user.application import module_wifi
from src.user.application.use_case.get_account import GetAccount


def request_wifi(user):
    usr, access, info = GetAccount().execute(permission='wifi', chat_id=user.id,
                                             name=user.first_name, username=user.username)

    call_sql(action="Wifi request", module=module_wifi, chat_id=user.id, type='user')

    response = []

    if access:
        response.append(
            f"🌐 Detalles de la red:\n----------------------------------\nSSID: {wifi_ssid()}\nPassword: {wifi_password()}\n----------------------------------\n⏬500mb\n⏫50mb\n🌐Wifi6")
        response.append(
            "📣 ¡Recuerda! Una vez ingreses con tus dispositivos 📱, tendrás 24hrs ⏰ para registrarlos en /dispositivos")
        response.append("Si no los registras serán bloqueados 📵 y perderás el acceso a la red")
        response.append("¡Disfruta de tú conexión! 😎")
    else:
        return get_unnaccess()

    return response
