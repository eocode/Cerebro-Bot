from sqlalchemy.orm import relationship

from src.shared.infrastructure.database.entity.home import Home

from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime

from sqlalchemy import Column, String, Float, ForeignKey
from datetime import datetime


class Product(Base):
    __tablename__ = "product"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False)
    amount = Column(Float, nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name, location_name):
        super().__init__()
        self.name = name
        self.location_name = location_name


class InventoryStatus(Base):
    __tablename__ = "inventory_status"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name):
        super().__init__()
        self.name = name


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(BIGINT, primary_key=True)

    home_id = Column(BIGINT, ForeignKey("home.id"))
    inventory_home = relationship(Home, foreign_keys=[home_id])
    product_id = Column(BIGINT, ForeignKey("product.id"))
    inventory_product = relationship(Product, foreign_keys=[product_id])
    status_id = Column(BIGINT, ForeignKey("inventory_status.id"))
    inventory_status = relationship(InventoryStatus, foreign_keys=[status_id])

    amount = Column(Float, nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, home_id, product_id, status_id, amount):
        super().__init__()
        self.home_id = home_id
        self.status_id = status_id
        self.product_id = product_id
        self.amount = amount
