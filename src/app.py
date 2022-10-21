from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler

from src.device.interface.device import DEVICES, PHOTO, LOCATION, BIO, skip_location, \
    location, photo, device, devices, skip_photo, bio
from src.device.interface.wifi import wifi
from src.payment.interface.payment import payment
from src.shared.infrastructure.bot.connector import application
from src.shared.interface.cancel import cancel_conversation
from src.shared.interface.messager import message_handler
from src.user.interface.login import account
from src.shared.interface.help import help_handler


def start_app():
    application.add_handler(CommandHandler(["cuenta"], account))
    application.add_handler(CommandHandler(["start"], help_handler))
    application.add_handler(CommandHandler(["ayuda"], help_handler))
    application.add_handler(CommandHandler(["pago"], payment))
    application.add_handler(CommandHandler(["wifi"], wifi))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("dispositivos", device)],
        states={
            DEVICES: [MessageHandler(filters.Regex("^(Mis dispositivos|Agregar uno nuevo)$"), devices)],
            PHOTO: [MessageHandler(filters.PHOTO, photo), CommandHandler("skip", skip_photo)],
            LOCATION: [
                MessageHandler(filters.LOCATION, location),
                CommandHandler("omitir", skip_location),
            ],
            BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
        },
        fallbacks=[CommandHandler("cancelar", cancel_conversation)],
    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT, message_handler))

    application.run_polling()
