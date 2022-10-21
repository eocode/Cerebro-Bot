from sqlalchemy.orm import relationship
from src.shared.infrastructure.database.entity.home import Home
from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime
from sqlalchemy import Column, String, ForeignKey
from datetime import datetime

from src.user.domain.Interface.iuser import IUser


class User(Base, IUser):
    __tablename__ = "user"
    id = Column(BIGINT, primary_key=True)

    chat_id = Column(BIGINT, nullable=False, unique=True)
    name = Column(String(300), nullable=False)
    last_name = Column(String(300), nullable=True)
    phone = Column(String(15), nullable=True)

    username = Column(String(15), default=False, nullable=True)

    home_id = Column(BIGINT, ForeignKey("home.id"))
    user_home = relationship(Home, foreign_keys=[home_id])

    is_verified = Column(Boolean, default=False)
    is_roomer = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, chat_id, name, username):
        super().__init__()
        self.chat_id = chat_id
        self.name = name
        self.username = username

    def __str__(self):
        return self.name + ' ' + self.last_name + ' con username: ' + self.username
