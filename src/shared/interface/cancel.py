import logging
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler

from src.device.application.request_wifi import request_wifi

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger()


async def cancel_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("Conversación terminada para %s.", user.first_name)
    await update.message.reply_text(
        "Estaré aquí cuando lo necesites.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
