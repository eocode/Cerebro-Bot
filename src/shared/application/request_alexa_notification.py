from sqlalchemy.sql.functions import count

from src.shared.application.query import call_sql
from src.shared.infrastructure.alexa_skills.send_proactive_message import send_proactive_message
from src.user.application.use_case.get_account import GetAccount


def request_alexa_notification(user, message):
    usr, access, info = GetAccount().execute(permission='settings', chat_id=user.id,
                                             name=user.first_name, username=user.username)

    call_sql(action="Notify", module='Alexa notifier', chat_id=user.id, type='user', message=message)

    response = []
    if access:
        if send_proactive_message(creator='casa', message=message) == 202:
            response.append("Notificación enviada")
        else:
            response.append("Error al enviar notificación")
    else:
        response.append("Tú cuenta aún no ha sido activada\nPor favor consulta más tarde\n")
        response.append("Puedes usar el comando /cuenta o /ayuda\n")

    return response
