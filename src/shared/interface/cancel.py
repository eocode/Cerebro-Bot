from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler

from src.device.application.request_wifi import request_wifi


async def cancel_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    await update.message.reply_text(
        "Estaré aquí cuando lo necesites.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
