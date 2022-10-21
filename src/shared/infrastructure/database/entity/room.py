from sqlalchemy.orm import relationship

from src.room.domain.interface.iroom import IRoom
from src.room.domain.interface.iroom_user import IRoomUser
from src.shared.infrastructure.database.entity.user import User
from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime
from src.shared.infrastructure.database.entity.home import Home
from sqlalchemy import Column, String, Float, ForeignKey
from datetime import datetime


class Room(Base, IRoom):
    __tablename__ = "room"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False, unique=True)
    bathroom = Column(BIGINT, nullable=False)
    kitchen = Column(BIGINT, nullable=False)
    patio = Column(BIGINT, nullable=False)
    capacity = Column(BIGINT, nullable=False)
    amount = Column(Float, nullable=False)

    home_id = Column(BIGINT, ForeignKey("home.id"))
    home_room_intermediate = relationship(Home, foreign_keys=[home_id])

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name, rooms, capacity, amount):
        super().__init__()
        self.name = name
        self.rooms = rooms
        self.capacity = capacity
        self.amount = amount


class RoomHistory(Base):
    __tablename__ = "room_history"
    id = Column(BIGINT, primary_key=True)

    room_id = Column(BIGINT, ForeignKey("room.id"))
    room_history_intermediate = relationship(Room, foreign_keys=[room_id])

    start_date = Column("start_date", DateTime, default=datetime.now())
    end_date = Column("end_date", DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
    is_first_month = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name, rooms, capacity, amount):
        super().__init__()
        self.name = name
        self.rooms = rooms
        self.capacity = capacity
        self.amount = amount


class RoomUser(Base, IRoomUser):
    __tablename__ = "room_user"
    id = Column(BIGINT, primary_key=True)

    user_id = Column(BIGINT, ForeignKey("user.id"))
    user_user_intermediate = relationship(User, foreign_keys=[user_id])
    room_id = Column(BIGINT, ForeignKey("room.id"))
    room_room_intermediate = relationship(Room, foreign_keys=[room_id])

    end_date = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, user_id, room_id):
        super().__init__()
        self.user_id = user_id
        self.room_id = room_id
