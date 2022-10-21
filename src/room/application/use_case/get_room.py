from src.shared.infrastructure.database.entity.room import RoomUser, Room, RoomHistory
from src.shared.application.query import call_sql
from src.room.application import module


class RoomInfo:

    def __init__(self, room):
        self.name = room.name
        self.start_date = room.start_date.date()
        self.end_date = None if room.end_date is None else room.end_date.date()


class GetRoom:

    @staticmethod
    def execute(chat_id, user_id) -> RoomInfo:
        q = call_sql(action="Get room of user", module=module, chat_id=chat_id, type='user')

        try:
            room = q.session.query(Room.name,
                                   RoomHistory.start_date,
                                   RoomHistory.end_date).join(RoomUser,
                                                              RoomUser.room_id == Room.id,
                                                              isouter=True).join(RoomHistory,
                                                                                 RoomHistory.room_id == Room.id,
                                                                                 isouter=True) \
                .filter(RoomUser.user_id == user_id).one()
            print(room)
            return RoomInfo(room)

        except Exception as e:
            print('Error al obtener la habitación del usuario')
            q.session.rollback()
            print(e)
