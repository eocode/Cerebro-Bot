from sqlalchemy.orm import relationship

from src.shared.infrastructure.database.entity.home import Home
from src.shared.infrastructure.database.entity.room import Room
from src.shared.infrastructure.database.entity.service import Service
from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime

from sqlalchemy import Column, String, ForeignKey, Integer
from datetime import datetime

from src.shared.infrastructure.database.entity.user import User


class IssueType(Base):
    __tablename__ = "issue_type"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False, unique=True)
    priority = Column(Integer, nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name, priority):
        super().__init__()
        self.name = name
        self.priority = priority


class Issue(Base):
    __tablename__ = "issue"
    id = Column(BIGINT, primary_key=True)

    user_id = Column(BIGINT, ForeignKey("user.id"))
    issue_user = relationship(User, foreign_keys=[user_id])
    room_id = Column(BIGINT, ForeignKey("room.id"))
    issue_room = relationship(Room, foreign_keys=[room_id])
    home_id = Column(BIGINT, ForeignKey("home.id"))
    issue_home = relationship(Home, foreign_keys=[home_id])
    service_id = Column(BIGINT, ForeignKey("service.id"))
    issue_service = relationship(Service, foreign_keys=[service_id])
    type_id = Column(BIGINT, ForeignKey("issue_type.id"))
    issue_type = relationship(IssueType, foreign_keys=[type_id])

    description = Column(String(300), nullable=False, unique=True)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, user_id, room_id, home_id, service_id, type_id):
        super().__init__()
        self.user_id = user_id
        self.room_id = room_id
        self.home_id = home_id
        self.service_id = service_id
        self.type_id = type_id
