from src.user.domain.Interface.iuser import IUser


class User(IUser):
    id = None
    name = None
    last_name = None
    phone = None
    username = None
    home_id = None
    is_verified = None
    is_roomer = None
    is_admin = None
    is_active = None
    created_at = None
    updated_at = None

    def __init__(self, chat_id, name):
        self.id = chat_id
        self.name = name

