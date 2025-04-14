import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.helpers import delete_message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a link and I'll try to download it")
    await delete_message(update, context, update.message.message_id)