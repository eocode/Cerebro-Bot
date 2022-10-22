from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from src.shared.application.request_help import request_help, request_start


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Un momento por favor ...")

    await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    for m in request_help(update.message.from_user):
        await update.message.reply_text(m)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bienvenid@ ...")

    await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    for m in request_start(update.message.from_user):
        await update.message.reply_text(m)
