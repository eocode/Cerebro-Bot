from sqlalchemy.orm import relationship

from src.shared.infrastructure.database.entity.home_service import HomeService
from src.shared.infrastructure.database.entity.inventory import Inventory
from src.shared.infrastructure.database.entity.room import Room
from src.shared.infrastructure.database.connector import Base
from sqlalchemy.sql.sqltypes import BIGINT, Boolean, DateTime

from sqlalchemy import Column, String, Float, ForeignKey
from datetime import datetime


class PaymentStatusEnum:
    Pending = 1
    Paid = 2
    Cancelled = 3


class PaymentStatus(Base):
    __tablename__ = "payment_status"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False, unique=True)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name):
        super().__init__()
        self.name = name


class Payment(Base):
    __tablename__ = "payment"
    id = Column(BIGINT, primary_key=True)

    room_id = Column(BIGINT, ForeignKey("room.id"))
    payment_room = relationship(Room)
    amount = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    extra_charges = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    status_id = Column(BIGINT, ForeignKey("payment_status.id"))
    payment_status = relationship(PaymentStatus)

    pay_date = Column(DateTime, default=datetime.now())
    billed_date = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, room_id, status_id, pay_date):
        super().__init__()
        self.room_id = room_id
        self.amount = 0
        self.discount = 0
        self.extra_charges = 0
        self.total = 0
        self.status_id = status_id
        self.pay_date = pay_date
        self.is_active = True


class PaymentConcept(Base):
    __tablename__ = "payment_concept"
    id = Column(BIGINT, primary_key=True)

    name = Column(String(300), nullable=False, unique=True)

    service_id = Column(BIGINT, ForeignKey("home_service.id"), nullable=True)
    payment_detail_service = relationship(HomeService, foreign_keys=[service_id])
    inventory_id = Column(BIGINT, ForeignKey("inventory.id"), nullable=True)
    payment_detail_inventory = relationship(Inventory, foreign_keys=[inventory_id])

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, name):
        super().__init__()
        self.name = name


class PaymentDetail(Base):
    __tablename__ = "payment_detail"
    id = Column(BIGINT, primary_key=True)

    payment_id = Column(BIGINT, ForeignKey("payment.id"))
    payment_detail_payment = relationship(Payment)
    concept_id = Column(BIGINT, ForeignKey("payment_concept.id"))
    payment_detail_concept = relationship(PaymentConcept)

    room_id = Column(BIGINT, ForeignKey("room.id"), nullable=True)
    payment_detail_room = relationship(Room, foreign_keys=[room_id])

    amount = Column(Float, nullable=False)

    is_monthly = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, payment_id, concept_id, amount, room_id, is_monthly):
        super().__init__()
        self.payment_id = payment_id
        self.concept_id = concept_id
        self.amount = amount
        self.room_id = room_id
        self.is_active = True
        self.is_monthly = is_monthly


class PaymentMonthly(Base):
    __tablename__ = "payment_monthly"
    id = Column(BIGINT, primary_key=True)

    room_id = Column(BIGINT, ForeignKey("room.id"), nullable=True)
    payment_detail_room = relationship(Room, foreign_keys=[room_id])

    concept_id = Column(BIGINT, ForeignKey("payment_concept.id"))
    payment_detail_concept = relationship(PaymentConcept)

    amount = Column(Float, nullable=False)

    start_date = Column("start_date", DateTime, default=datetime.now())
    end_date = Column("end_date", DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, payment_id, concept_id, amount, service_id, room_id, inventory_id):
        super().__init__()
        self.payment_id = payment_id
        self.concept_id = concept_id
        self.amount = amount
        self.service_id = service_id
        self.room_id = room_id
        self.inventory_id = inventory_id


class PaymentDeposit(Base):
    __tablename__ = "payment_deposit"
    id = Column(BIGINT, primary_key=True)

    payment_id = Column(BIGINT, ForeignKey("payment.id"))
    payment_deposit_payment = relationship(Payment)

    room_id = Column(BIGINT, ForeignKey("room.id"))
    payment_room = relationship(Room)

    amount = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    status_id = Column(BIGINT, ForeignKey("payment_status.id"))
    payment_status = relationship(PaymentStatus)

    pay_date = Column(DateTime, default=datetime.now())
    billed_date = Column(DateTime, nullable=True)
    refund_date = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())

    def __init__(self, payment_id, room_id, amount, status_id, pay_date):
        super().__init__()
        self.payment_id = payment_id
        self.room_id = room_id
        self.amount = amount
        self.discount = 0
        self.total = amount
        self.status_id = status_id
        self.pay_date = pay_date
        self.is_active = True
