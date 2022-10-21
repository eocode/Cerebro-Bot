from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from src.user.application.request_account import request_account


async def account(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("Un momento por favor ...")

    await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    for m in request_account(update.message.from_user):
        await update.message.reply_text(m)
