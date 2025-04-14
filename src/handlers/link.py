import os
import re
import logging
from telegram import Update
from utils.helpers import delete_message
from telegram.ext import ContextTypes, filters
from utils.downloader import download_audio, download_video_from_instagram, download_video_from_tiktok


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    user_message_id = update.message.message_id
    chat_id = update.message.chat_id

    downloading_msg = await update.message.reply_text(f"Downloading...")

    if "instagram.com/" in url:
        filepath = download_video_from_instagram(url)
        filetype = "video"
    elif "tiktok.com/" in url:
        filepath = download_video_from_tiktok(url)
        filetype = "video"
    else:
        filepath = download_audio(url)
        filetype = "audio"

    if filepath and os.path.exists(filepath):
        try: 
            if filetype == "video":
                await context.bot.send_video(chat_id=chat_id, video=open(filepath, "rb"))
            else: 
                await update.message.reply_audio(audio=open(filepath, "rb"))
        finally:
            os.remove(filepath)
            logging.info(f"Removed {filepath}")
            await delete_message(update, context, user_message_id)
            await delete_message(update, context, downloading_msg.message_id)
    else:
        await update.message.reply_text("Download failed")

url_filter = filters.Regex(re.compile(r"https?://\S+"))