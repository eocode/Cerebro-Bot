from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from src.payment.application.request_payment import request_payment


async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("Consultando información del pago ...")

    await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    for m in request_payment(update.message.from_user):
        await update.message.reply_text(m)
