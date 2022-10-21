from src.shared.application.query import call_sql
from src.payment.application import module
from src.shared.infrastructure.database import Payment, PaymentConcept, PaymentDetail


class GetPaymentDetail:

    @staticmethod
    def execute(chat_id, room_id, payment_id):
        q = call_sql(action="Get Payment", module=module, chat_id=chat_id, type='user')

        try:
            return q.session.query(PaymentDetail.__table__, PaymentConcept.name.label('concept_name')).join(
                PaymentConcept,
                PaymentConcept.id == PaymentDetail.concept_id, isouter=True
            ).filter(
                PaymentDetail.room_id == room_id,
                PaymentDetail.payment_id == payment_id,
                PaymentDetail.is_active == True
            ).all()
        except Exception as e:
            print('Error al Obtener detalles del pago')
            q.session.rollback()
            print(e)
