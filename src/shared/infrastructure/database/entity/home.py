from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime

from sqlalchemy import Column, String
from datetime import datetime


class Home(Base):
    __tablename__ = "home"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False)
    location_name = Column(String(300), nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name, location_name):
        super().__init__()
        self.name = name
        self.location_name = location_name
