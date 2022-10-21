import enum
from sqlalchemy import Enum
from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, DateTime

from sqlalchemy import Column, String
from datetime import datetime


class Type(enum.Enum):
    system = "System"
    user = "User"


class Logging(Base):
    __tablename__ = "logging"
    id = Column(BIGINT, primary_key=True)
    module = Column(String(300), nullable=False)
    action = Column(String(300), nullable=False)
    ref_user_id = Column(BIGINT, nullable=True)

    message = Column(String(600), nullable=True)

    type = Column(Enum(Type))

    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, module, action, ref_user_id, type, message=None):
        super().__init__()
        self.module = module
        self.action = action
        self.ref_user_id = ref_user_id
        self.type = type
        self.message = message
