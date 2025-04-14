import os
import logging
from yt_dlp import YoutubeDL
from config.settings import DOWNLOAD_DIR
from utils.cache import load_cache, save_cache

def download_audio(url):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    cache = load_cache()

    if url in cache and os.path.exists(cache[url]):
        print("Already downloaded")
        return cache[url]
    
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info).rsplit(".", 1)[0]+".mp3"
            cache[url] = filename
            save_cache(cache)
            return filename
    except Exception as e:
        logging.exception("Download error: {e}")
        return None


def download_video_from_instagram(url):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    ydl_opts = {
        "format": "best[ext=mp4]/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "quiet": False,
        "no_warnings": False,
    }

    try: 
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        logging.exception(f"Instagram video download error: {e}")
        return None

def download_video_from_tiktok(url):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "merge_output_format": "mp4",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        logging.exception(f"TikTok video download error: {e}")
        return None