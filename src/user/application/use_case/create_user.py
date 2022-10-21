from src.shared.application.query import call_sql
from src.user.application import module
from src.shared.infrastructure.database.entity.user import User


class CreateUser:

    @staticmethod
    def execute(chat_id, name, username):
        q = call_sql(action="Create a user by ID", module=module, type='user', chat_id=chat_id)
        try:
            account = User(chat_id=chat_id, name=name, username=username)
            q.session.merge(account)
            q.session.commit()
            return True
        except Exception as e:
            print('Error al crear el usuario')
            q.session.rollback()
            print(e)
