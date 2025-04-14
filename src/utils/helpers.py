import logging
from telegram import Update
from telegram.ext import ContextTypes

def format_duration(seconds):
    if not seconds:
        return "?:??"
    seconds = int(seconds)
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins}:{secs:02d}"

async def delete_message(update: Update, context: ContextTypes.DEFAULT_TYPE, message_id:int):
    try:
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message_id)
    except Exception as e:
        logging.warning(f"Could not delete message {message_id}: {e}")
        