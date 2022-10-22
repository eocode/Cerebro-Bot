from typing import Dict

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.constants import ChatAction
from telegram.ext import ContextTypes, ConversationHandler

from src.device.application.request_wifi import request_wifi
from src.shared.infrastructure.validators.validate_mac import is_valid_mac_address

ACTIONABLE, ADD_MAC, SAVE_DEVICE = range(3)
options = ["Mis dispositivos", "Agregar uno nuevo"]

data = {}


async def device(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the conversation and asks the user about their gender."""

    options = ["Mis dispositivos", "Agregar uno nuevo"]

    reply_keyboard = [
        options,
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    await update.message.reply_text(
        "🧾 Registra y gestiona tus dispositivos aquí.\n"
        "Por favor selecciona una opción para continuar:",
        reply_markup=markup,
    )

    return ACTIONABLE


async def show_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""
    text = update.message.text

    if text == options[0]:
        await update.message.reply_text(
            "A continuación te mostraremos tus dispositivos agregados",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    if text == options[1]:
        types = ['Telefono', 'PC']
        reply_keyboard = [
            types,
        ]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "📱 Elige el tipo de dispositivo que agregarás.\n"
            "La red se optimizará para el tipo de dispositivo que agregues",
            reply_markup=markup,
        )

        return ADD_MAC


async def add_mac(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""

    type = update.message.text
    data[update.message.chat_id] = type

    print(type)

    await update.message.reply_text(
        "Agregaremos un nuevo dispositivo",
        reply_markup=ReplyKeyboardRemove()
    )
    await update.message.reply_text(
        'Escribe la dirección MAC'
    )

    return SAVE_DEVICE


async def save_device(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""

    mac = update.message.text
    print(mac, data.get(update.message.chat_id))

    if is_valid_mac_address(mac):
        await update.message.reply_text(
            'Dirección valida',
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await update.message.reply_text(
            '❌ Dirección MAC invalida\nIntenta de nuevo en /dispositivos',
            reply_markup=ReplyKeyboardRemove()
        )

    return ConversationHandler.END


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]

    await update.message.reply_text(
        f"I learned these facts about you: {user_data}Until next time!",
        reply_markup=ReplyKeyboardRemove(),
    )

    user_data.clear()
    return ConversationHandler.END
