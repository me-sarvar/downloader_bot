import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DOWNLOAD_DIR = "downloads"
COOKIES_DIR = "cookies"
CACHE_FILE = "cache.json"
MAX_DURATION = 600