from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Telegram Bot Token (use your real one here)
TOKEN = '7594237181:AAHwlqXJo43nP8q5qNc_HK505j-uGLhkERM'

# Enable logging to Railway console
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    logger.info("User started the bot.")
    update.message.reply_text("👋 Welcome! Send me any Instagram reel link to download.")

def handle_message(update, context):
    text = update.message.text
    chat_id = update.message.chat_id
    logger.info(f"Received message: {text} from {chat_id}")

    if "instagram.com/reel" in text:
        update.message.reply_text("📥 Downloading reel... (Feature coming soon)")
    else:
        update.message.reply_text("❌ Please send a valid Instagram reel link.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    logger.info("Bot started polling...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
