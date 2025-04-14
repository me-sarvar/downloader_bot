import os
import yt_dlp
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from config.settings import DOWNLOAD_DIR
from utils.helpers import delete_message
from concurrent.futures import ThreadPoolExecutor
from handlers.shared import SEARCH_RESULTS, executor

async def handle_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if not query.data.startswith("select_"):
        return

    index = int(query.data.split("_")[1])
    chat_id = query.message.chat_id
    results = SEARCH_RESULTS.get(chat_id)

    if not results or index >= len(results):
        await query.edit_message_text("⚠️ That option expired or is invalid.")
        return

    result = results[index]
    url = result.get("url") or result.get("webpage_url")
    title = result["title"]

    await query.edit_message_text(f"⬇️ Downloading: {title}")
    download_msg = query.message

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    loop = asyncio.get_event_loop()

    def download_song():
        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "128",
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            filename = filename.replace(".webm", ".mp3").replace(".m4a", ".mp3")
            return filename, info

    try:
        filename, info = await loop.run_in_executor(executor, download_song)
        await query.message.reply_audio(audio=open(filename, "rb"), title=info["title"])
        os.remove(filename)
    except Exception as e:
        print(f"[ERROR] {e}")
        await query.message.reply_text("❌ Could not download this song.")
    finally:
        await delete_message(update, context, download_msg.message_id)