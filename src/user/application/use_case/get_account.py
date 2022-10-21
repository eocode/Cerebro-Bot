from typing import Tuple

from src.shared.application.query import call_sql
from src.user.application import module_auth
from src.user.application.use_case.create_user import CreateUser
from src.user.application.use_case.get_user import GetUser
from src.user.domain.Interface.iuser import IUser

permissions = {
    "guest": ['account'],
    "roomer": ['account', 'settings', 'invoice', 'wifi', 'issues', 'devices', 'carboy'],
    "admin": ['account', 'settings', 'invoice', 'wifi', 'issues', 'devices', 'carboy']
}


class DetailedInfo:

    def __init__(self, is_verified, phone, name, last_name, room_id, room_name, start_date, end_date, is_first_month):
        self.verify = 'Sí' if is_verified else 'No'
        self.phone = 'Sin registrar' if phone is None else phone
        self.full_name = ('' if name is None else name) + ' ' + ('' if last_name is None else last_name)
        self.room_id = room_id
        self.room_name = room_name
        self.room_start_date = start_date.date()
        self.room_end_date = None if end_date is None else end_date.date()
        self.is_first_month = is_first_month


class GetAccount:

    @staticmethod
    def execute(chat_id, permission, name, username) -> tuple[IUser, bool, DetailedInfo]:
        access = False
        q = call_sql(action="Verify User Access", module=module_auth, chat_id=chat_id, type='system')
        role = 'guest'
        try:
            user = GetUser().execute(chat_id=chat_id)
            if user is None:
                CreateUser().execute(chat_id=chat_id, name=name, username=username)
                user = GetUser().execute(chat_id=chat_id), access

            if user.is_roomer:
                role = 'roomer'

            if user.is_admin:
                role = 'admin'

            if not user.is_verified:
                role = 'guest'

            if permission in permissions[role]:
                access = True

            d_info = DetailedInfo(user.is_verified, user.phone, user.name, user.last_name, user.room_id,
                                  user.room_name, user.room_start_date, user.room_end_date, user.is_first_month)

            return user, access, d_info

        except Exception as e:
            print('Error en autenticación y revisión de permisos')
            q.session.rollback()
            print(e)
