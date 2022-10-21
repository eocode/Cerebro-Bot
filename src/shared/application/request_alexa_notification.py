from sqlalchemy.sql.functions import count

from src.shared.application.query import call_sql
from src.shared.infrastructure.alexa_skills.send_proactive_message import send_proactive_message
from src.shared.infrastructure.cognitive.responses.account import get_unnaccess
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
        return get_unnaccess()

    return response
