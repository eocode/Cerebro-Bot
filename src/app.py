from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler

from src.device.interface.device import device, done, ACTIONABLE, show_response, ADD_MAC, add_mac, SAVE_DEVICE, \
    save_device
from src.device.interface.wifi import wifi
from src.payment.interface.payment import payment
from src.shared.infrastructure.bot.connector import application
from src.shared.interface.messager import message_handler
from src.user.interface.login import account
from src.shared.interface.help import help_handler, start_handler


def start_app():
    application.add_handler(CommandHandler(["start"], start_handler))
    application.add_handler(CommandHandler(["cuenta"], account))
    application.add_handler(CommandHandler(["ayuda"], help_handler))
    application.add_handler(CommandHandler(["pago"], payment))
    application.add_handler(CommandHandler(["wifi"], wifi))

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("dispositivos", device)],
        states={
            # CHOOSING: [
            #     MessageHandler(
            #         filters.Regex("^(Age|Favourite colour|Number of siblings)$"), regular_choice
            #     ),
            #     MessageHandler(filters.Regex("^Something else...$"), custom_choice),
            # ],
            # TYPING_CHOICE: [
            #     MessageHandler(
            #         filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), regular_choice
            #     )
            # ],
            ACTIONABLE: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    show_response,
                )
            ],
            ADD_MAC: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    add_mac,
                )
            ],
            SAVE_DEVICE: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    save_device,
                )
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Cancelar$"), done)],
    )
    application.add_handler(conv_handler)

    application.add_handler(MessageHandler(filters.TEXT, message_handler))

    application.run_polling()
