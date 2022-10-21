from sqlalchemy.orm import relationship
from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from datetime import datetime
from src.shared.infrastructure.database.entity.user import User


class DeviceType(Base):
    __tablename__ = "device_type"
    id = Column(BIGINT, primary_key=True)  # CID user

    name = Column(String(300), nullable=False, unique=True)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name):
        super().__init__()
        self.name = name


class Device(Base):
    __tablename__ = "device"
    id = Column(BIGINT, primary_key=True)

    user_id = Column(BIGINT, ForeignKey("user.id"))
    mac = Column(String(300), nullable=False)
    type_id = Column(BIGINT, ForeignKey("device_type.id"))

    user_device = relationship(User, foreign_keys=[user_id])
    device_type = relationship(DeviceType, foreign_keys=[type_id])
    UniqueConstraint('user_id', 'mac', name='user_mac')

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, user_id, mac, type_id):
        super().__init__()
        self.user_id = user_id
        self.mac = mac
        self.type_id = type_id
