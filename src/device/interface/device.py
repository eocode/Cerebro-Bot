import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.constants import ChatAction
from telegram.ext import ContextTypes, ConversationHandler

from src.device.application.request_wifi import request_wifi

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger()

DEVICES, PHOTO, LOCATION, BIO = range(4)
OPTIONS = ["Mis dispositivos", "Agregar uno nuevo"]


async def device(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [OPTIONS]

    await update.message.reply_text(
        "En está sección podrás agregar y ver los dispositivos que has registrado.\n\n"
        "Envia /cancelar para terminar la conversación.\n\n"
        "Por favor selecciona una opción para continuar:",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Elije:"
        ),
    )

    return DEVICES


async def devices(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    message = update.message.text
    logger.info("Selección %s: %s", user.first_name, message)
    if message == OPTIONS[0]:
        await update.message.reply_text(
            f"Elegiste: {message}"
        )
        return PHOTO
    if update.message.text == OPTIONS[1]:
        await update.message.reply_text(
            f"Elegiste: {message}"
        )
        return PHOTO


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download("user_photo.jpg")
    logger.info("Photo of %s: %s", user.first_name, "user_photo.jpg")
    await update.message.reply_text(
        "Gorgeous! Now, send me your location please, or send /skip if you don't want to."
    )

    return LOCATION


async def skip_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    await update.message.reply_text(
        "I bet you look great! Now, send me your location please, or send /skip."
    )

    return LOCATION


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    await update.message.reply_text(
        "Maybe I can visit you sometime! At last, tell me something about yourself."
    )

    return BIO


async def skip_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the location and asks for info about the user."""
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    await update.message.reply_text(
        "You seem a bit paranoid! At last, tell me something about yourself."
    )

    return BIO


async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Thank you! I hope we can talk again some day.")

    return ConversationHandler.END
