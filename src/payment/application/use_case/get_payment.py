from src.shared.infrastructure.database.entity.payment import Payment
from src.shared.application.query import call_sql
from src.payment.application import module


class GetPayment:

    @staticmethod
    def execute(chat_id, room_id):
        q = call_sql(action="Get Payment", module=module, chat_id=chat_id, type='user')
        try:
            return q.session.query(Payment.__table__).filter(
                Payment.room_id == room_id,
                Payment.billed_date == None,
                Payment.is_active == True).one()
        except Exception as e:
            print('Error al obtener el pago')
            q.session.rollback()
            print(e)

