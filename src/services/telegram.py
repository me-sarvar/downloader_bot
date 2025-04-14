from handlers.start import start
from config.settings import BOT_TOKEN
from handlers.search import search_song
from handlers.selection import handle_selection
from handlers.link import handle_link, url_filter
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters

def create_application():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(url_filter & ~filters.COMMAND, handle_link))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_song))
    app.add_handler(CallbackQueryHandler(handle_selection))

    return app