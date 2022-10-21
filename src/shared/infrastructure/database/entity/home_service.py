from sqlalchemy.orm import relationship

from src.shared.infrastructure.database.entity.service import Service
from src.shared.infrastructure.database.entity.home import Home
from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime

from sqlalchemy import Column, String, ForeignKey, Float
from datetime import datetime


class HomeService(Base):
    __tablename__ = "home_service"
    id = Column(BIGINT, primary_key=True)

    home_id = Column(BIGINT, ForeignKey("home.id"), nullable=False)
    home_service_intermediate = relationship(Home, foreign_keys=[home_id])
    service_id = Column(BIGINT, ForeignKey("service.id"), nullable=False)
    service_home_intermediate = relationship(Service, foreign_keys=[service_id])

    description = Column(String(300), nullable=True)
    capacity = Column(BIGINT, nullable=False)
    amount = Column(Float, nullable=False)

    is_active = Column(Boolean, default=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, home_id, service_id, description, amount, capacity):
        super().__init__()
        self.home_id = home_id
        self.service_id = service_id
        self.description = description
        self.capacity = capacity
        self.amount = amount
