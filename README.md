# Music Downloader Bot

A Telegram bot that downloads audio and video from YouTube, Instagram, and TikTok.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/music_downloader_bot.git
   cd music_downloader_bot
   ```
2. Install dependencies:
    ``` bash
    pip install -r requirements.txt
    ```
3. Create a .env file with your Telegram bot token:
    ```bash
    BOT_TOKEN=your_bot_token_here
    ```
4. Run the bot:
    ```bash
    python src/main.py
    ```

## Features
- Search for songs on YouTube and download as MP3.
- Download videos from Instagram and TikTok.
- Cache downloaded files to avoid redundant downloads.


## License
```text

---

### Additional Improvements

1. **Logging**:
   - Replace `print` statements with `logging` for better debugging and monitoring.
   - Configure logging levels (e.g., `DEBUG`, `INFO`, `ERROR`) in `src/main.py`.

2. **Error Handling**:
   - Add more specific error messages for users (e.g., "Invalid URL format" or "Download timeout").
   - Use try-except blocks consistently across all functions.

3. **Caching**:
   - The `SEARCH_RESULTS` dictionary is currently stored in memory. Consider using a persistent storage solution (e.g., SQLite or Redis) for larger-scale use.
   - Add cache expiration for downloaded files to manage disk space.

4. **ThreadPoolExecutor**:
   - The `ThreadPoolExecutor` is defined in multiple files. Consider creating a singleton or passing it as a parameter to avoid redundant instances.

5. **Testing**:
   - Add unit tests in a `tests/` directory using `pytest` to verify download and handler logic.
   - Mock external services (e.g., YouTube, Telegram) for testing.

6. **Code Style**:
   - Use a linter like `flake8` or `pylint` to enforce consistent code style.
   - Run `black` or `isort` for automatic code formatting.

7. **Documentation**:
   - Add docstrings to all functions and modules.
   - Use type hints for better code clarity (e.g., `def download_audio(url: str) -> Optional[str]`).

8. **Security**:
   - Validate URLs before processing to prevent injection attacks.
   - Limit file sizes to avoid memory issues.

---

### How to Transition to This Structure

1. **Create the Directory Structure**:
   - Use the command line or your IDE to create the folders and files as shown above.

2. **Move Existing Code**:
   - Copy and paste the relevant code snippets into the new files.
   - Update imports to reflect the new structure (e.g., `from src.utils.downloader import download_audio`).

3. **Test the Bot**:
   - Run `python src/main.py` to ensure everything works.
   - Debug any import errors or missing dependencies.

4. **Install Dependencies**:
   - Create `requirements.txt` and run `pip install -r requirements.txt`.

5. **Version Control**:
   - Initialize a Git repository and commit the changes.
   - Push to a remote repository (e.g., GitHub) for backup.

---

This structure separates concerns, improves readability, and makes the project easier to maintain or extend. Let me know if you need help with any specific part of the implementation!
```