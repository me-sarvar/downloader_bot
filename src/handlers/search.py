import asyncio
import yt_dlp
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from config.settings import MAX_DURATION
from utils.helpers import format_duration, delete_message
from concurrent.futures import ThreadPoolExecutor
from handlers.shared import SEARCH_RESULTS, executor

async def search_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    user_msg = update.message
    search_msg = await update.message.reply_text(f"🔍 Searching for: {query}")

    loop = asyncio.get_event_loop()
    try:
        def yt_search():
            with yt_dlp.YoutubeDL({
                "quiet": True,
                "extract_flat": True,
                "skip_download": True
            }) as ydl:
                return ydl.extract_info(f"ytsearch30:{query}", download=False)

        raw_info = await loop.run_in_executor(executor, yt_search)
        raw_results = raw_info["entries"]

        filtered = []
        for entry in raw_results:
            duration = entry.get("duration")
            if duration is None or duration > MAX_DURATION:
                continue
            filtered.append(entry)
            if len(filtered) == 10:
                break

        if not filtered:
            await search_msg.edit_text("⚠️ No songs under 10 minutes found.")
            return

        SEARCH_RESULTS[update.effective_chat.id] = filtered

        buttons = [
            [InlineKeyboardButton(f"{e['title']} ({format_duration(e['duration'])})", callback_data=f"select_{i}")]
            for i, e in enumerate(filtered)
        ]
        markup = InlineKeyboardMarkup(buttons)

        await search_msg.edit_text("🎶 Choose a version:", reply_markup=markup)

    except Exception as e:
        print(f"[ERROR] {e}")
        await search_msg.edit_text("❌ Error while searching. Try again later.")
    finally:
        await delete_message(update, context, user_msg.message_id)