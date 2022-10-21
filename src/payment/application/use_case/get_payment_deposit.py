from src.shared.infrastructure.database import PaymentDeposit
from src.shared.infrastructure.database.entity.payment import Payment
from src.shared.application.query import call_sql
from src.payment.application import module


class GetPaymentDeposit:

    @staticmethod
    def execute(chat_id, room_id):
        q = call_sql(action="Get Payment Deposit", module=module, chat_id=chat_id, type='user')
        try:
            return q.session.query(PaymentDeposit.__table__).filter(
                PaymentDeposit.room_id == room_id,
                PaymentDeposit.status_id == 1,
                PaymentDeposit.billed_date == None,
                PaymentDeposit.is_active).one()
        except Exception as e:
            print('Error al obtener el deposito')
            q.session.rollback()
            print(e)

