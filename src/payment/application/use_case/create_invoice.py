from sqlalchemy.sql import functions

from src.shared.infrastructure.database import PaymentMonthly, PaymentDetail, RoomHistory, PaymentDeposit
from src.shared.infrastructure.database.entity.payment import Payment, PaymentStatusEnum
from src.shared.application.query import call_sql
from src.payment.application import module
from datetime import datetime, timedelta


class CreateInvoice:

    @staticmethod
    def execute(chat_id, room_id, is_first_month, start_date):
        q = call_sql(action="Create Invoice", module=module, chat_id=chat_id, type='user')
        try:
            # Create payment
            if is_first_month:
                date = datetime.now()
                date = (date.replace(day=start_date.day))
            else:
                date = datetime.now()
                date = (date.replace(day=1) + timedelta(days=32)).replace(day=1)
            invoice = Payment(room_id=room_id, status_id=PaymentStatusEnum.Pending,
                              pay_date=date)
            q.session.add(invoice)

            # Create detail
            monthly_payments = q.session.query(PaymentMonthly.__table__).filter(PaymentMonthly.room_id == room_id,
                                                                                Payment.is_active).all()
            amount = 0.0
            for row in monthly_payments:
                amount = amount + row.amount
                detail = PaymentDetail(payment_id=invoice.id, amount=row.amount, concept_id=row.concept_id,
                                       room_id=room_id, is_monthly=True)
                q.session.add(detail)

            # Update payment amount
            if is_first_month:
                total = float((amount / 30) * (31 - start_date.day))
                discount = float(amount - total)
            else:
                discount = float(0.0)
                total = float(amount)

            # Extra charges
            extra = q.session.query(functions.sum(PaymentDetail.amount)) \
                .filter(PaymentDetail.room_id == room_id,
                        PaymentDetail.is_active,
                        PaymentDetail.is_monthly is False) \
                .scalar()

            extra = float(extra) if extra is not None else 0.0

            # Update payment
            q.session.query(Payment.__table__).filter_by(id=invoice.id).update(
                {'amount': float(amount), 'discount': float(discount), 'extra_charges': float(extra),
                 'total': float(total + extra)})

            # Update first payment
            if is_first_month:
                q.session.query(RoomHistory.__table__).filter_by(id=room_id).update(
                    {'is_first_month': 0})
                deposit = PaymentDeposit(payment_id=invoice.id, room_id=room_id, amount=amount,
                                         status_id=PaymentStatusEnum.Pending,
                                         pay_date=date)
                q.session.add(deposit)

            q.session.commit()
            return True
        except Exception as e:
            print('Error al crear la factura')
            q.session.rollback()
            print(e)
            return False
