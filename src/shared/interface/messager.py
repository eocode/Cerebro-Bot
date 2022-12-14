from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import CallbackContext

from src.payment.application.request_payment import request_payment
from src.shared.application.request_alexa_notification import request_alexa_notification
from src.shared.application.request_help import request_help
from src.shared.application.use_case.log_message import LogMessage
from src.shared.infrastructure.cognitive.responses.error import get_error_message
from src.shared.infrastructure.cognitive.responses.greetings import get_greeting, GREETINGS
from src.shared.infrastructure.cognitive.responses.helpers import HELPERS, get_help
from src.shared.infrastructure.cognitive.responses.network import WIFI, get_wifi
from src.shared.infrastructure.cognitive.responses.notify import NOTIFY
from src.shared.infrastructure.cognitive.responses.payment import PAYMENTS, get_payment
from src.shared.infrastructure.cognitive.responses.thanks import THANKS, get_thanks
from src.device.application.request_wifi import request_wifi


async def message_handler(update: Update, context: CallbackContext) -> None:
    """this function messages at a specific time"""

    await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    LogMessage().execute(chat_id=update.message.chat_id, message=update.message.text)
    name = update.message.from_user.first_name

    response = False

    # Basic conversation
    if any(word in update.message.text.lower() for word in GREETINGS):
        await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        await update.message.reply_text(get_greeting(name))
        response = True

    if any(word in update.message.text.lower() for word in HELPERS):
        await update.message.reply_text(get_help(name))
        await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)

        for m in request_help(update.message.from_user):
            await update.message.reply_text(m)
        response = True

    if any(word in update.message.text.lower() for word in THANKS):
        await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        await update.message.reply_text(get_thanks(name))
        response = True

    # Room functionality
    if any(word in update.message.text.lower() for word in WIFI):
        await update.message.reply_text(get_wifi(name))
        await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        for m in request_wifi(update.message.from_user):
            await update.message.reply_text(m)
        response = True

    if any(word in update.message.text.lower() for word in PAYMENTS):
        await update.message.reply_text(get_payment(name))
        await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        for m in request_payment(update.message.from_user):
            await update.message.reply_text(m)
        response = True

    # Smart Alerts
    if any(word in update.message.text.lower() for word in NOTIFY):
        await context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        for m in request_alexa_notification(update.message.from_user, 'A??n no has pagado la luz'):
            await update.message.reply_text(m)
        response = True

    # Without Response
    if not response:
        await update.message.reply_text(get_error_message(name))
