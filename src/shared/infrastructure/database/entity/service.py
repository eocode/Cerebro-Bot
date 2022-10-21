from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime

from sqlalchemy import Column, String
from datetime import datetime


class Service(Base):
    __tablename__ = "service"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False, unique=True)

    is_billed = Column(Boolean, default=True)
    is_optional = Column(Boolean, default=False, nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name):
        super().__init__()
        self.name = name