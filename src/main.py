import logging
from services.telegram import create_application

logging.basicConfig(level=logging.INFO)

def main():
    app=create_application()
    app.run_polling()

if __name__ == "__main__":
    main()