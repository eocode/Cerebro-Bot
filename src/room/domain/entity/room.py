from src.room.domain.interface.iroom import IRoom


class Room(IRoom):
    id = None
    name = None
    rooms = None
    capacity = None
    amount = None
    home_id = None
    bathroom = None
    kitchen = None
    patio = None
    is_active = None
    created_at = None
    updated_at = None
