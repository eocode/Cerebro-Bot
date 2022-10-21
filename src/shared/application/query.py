from src.shared.infrastructure.database.entity.logging import Logging, Type
from src.shared.infrastructure.database.connector import SQLConnector


def get_type():
    return Type


def call_sql(action: str, module, chat_id, type, message=None) -> SQLConnector:
    obj = SQLConnector(action)
    try:
        log = Logging(action=action, module=module, ref_user_id=chat_id, type=type, message=message)
        obj.session.add(log)
        obj.session.commit()
    except Exception as e:
        obj.session.rollback()
        print('Error Logging: ')
        print(e)
    return obj

# def call_sql_thread(action: str):
#     return Thread(target=call_sql(action))
