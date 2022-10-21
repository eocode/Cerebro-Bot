import logging
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from src.device.application.request_wifi import request_wifi

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger()


async def wifi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("Obteniendo datos de la red ...")

    await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    for m in request_wifi(update.message.from_user):
        await update.message.reply_text(m)
