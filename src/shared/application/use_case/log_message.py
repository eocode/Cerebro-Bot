from src.shared.application.query import call_sql
from src.shared.application import module


class LogMessage:

    @staticmethod
    def execute(chat_id, message):
        q = call_sql(action="User input", module=module, chat_id=chat_id, type='user', message=message)

        try:
            return True
        except Exception as e:
            print('Error al loggear mensage')
            q.session.rollback()
            print(e)
