from src.room.domain.interface.iroom_user import IRoomUser


class RoomUser(IRoomUser):
    id = None
    user_id = None
    room_id = None
    end_date = None
    is_active = None
    created_at = None
    updated_at = None
