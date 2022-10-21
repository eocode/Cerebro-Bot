from src.shared.infrastructure.database.entity.room import RoomUser, Room, RoomHistory
from src.shared.application.query import call_sql
from src.user.application import module
from src.shared.infrastructure.database.entity.user import User


class GetUser:

    @staticmethod
    def execute(chat_id):
        q = call_sql(action="Get user info", module=module, type='user', chat_id=chat_id)
        try:
            return q.session.query(User.__table__, Room.id.label('room_id'), Room.name.label('room_name'),
                                   RoomHistory.start_date.label('room_start_date'),
                                   RoomHistory.end_date.label('room_end_date'),
                                   RoomHistory.is_first_month.label('is_first_month')).join(
                RoomUser,
                RoomUser.user_id == User.id, isouter=True).join(RoomHistory, RoomHistory.room_id == RoomUser.room_id,
                                                                isouter=True).join(
                Room, RoomUser.room_id == Room.id).filter(
                User.chat_id == chat_id, User.is_active).one()
        except Exception as e:
            print('Error al obtener el usuario')
            q.session.rollback()
            print(e)
