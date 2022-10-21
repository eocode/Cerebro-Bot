from logging import info

from src.payment.application.use_case.create_invoice import CreateInvoice
from src.payment.application.use_case.get_payment import GetPayment
from src.payment.application.use_case.get_payment_deposit import GetPaymentDeposit
from src.payment.application.use_case.get_payment_detail import GetPaymentDetail
from src.user.application.use_case.get_account import GetAccount


def request_payment(user):
    usr, access, info = GetAccount().execute(permission='invoice', chat_id=user.id,
                                             name=user.first_name, username=user.username)

    response = []

    if access:
        print('Obteniendo el pago')
        invoice = GetPayment().execute(chat_id=user.id, room_id=info.room_id)
        print(invoice)
        if invoice is None:
            pass
            print('Creando factura')
            CreateInvoice.execute(chat_id=user.id, room_id=info.room_id, is_first_month=info.is_first_month,
                                  start_date=info.room_start_date)
            invoice = GetPayment().execute(chat_id=user.id, room_id=info.room_id)

        response.append(
            f"🏡 {info.room_name}\n⏰ A pagar el {invoice.pay_date.date()}\n")

        invoice_detail = GetPaymentDetail.execute(chat_id=user.id, room_id=info.room_id, payment_id=invoice.id)
        details = ""
        for items in invoice_detail:
            details += f"{items.concept_name}, "
        details = details[:-2]
        response.append(f"Renta: ${int(invoice.amount) - int(invoice.discount)} MXN\n{details}")

        deposit = GetPaymentDeposit.execute(chat_id=user.id, room_id=info.room_id)

        response.append(f"Extras: ${int(invoice.extra_charges)} MXN\nDias de retraso")

        if deposit is not None:
            response.append(
                f"Deposito: {deposit.amount}\nSe devuelve en su totalidad al entregar tal como se recibió")
            response.append(
                f"Total del periodo: {invoice.total + deposit.amount}\n")
        else:
            response.append(
                f"Total del periodo: ${invoice.total} MXN\n")

    return response
