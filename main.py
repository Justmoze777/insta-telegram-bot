from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from instagrapi import Client

# Setup
USERNAME = "mynameispravinbhai"
PASSWORD = "Pass@131313"
TELEGRAM_TOKEN = "7594237181:AAHwlqXJo43nP8q5qNc_HK505j-uGLhkERM"

cl = Client()
cl.login(USERNAME, PASSWORD)

def start(update, context):
    update.message.reply_text("👋 Send a reel link to get HD download.")

def download_reel(update, context):
    url = update.message.text.strip()

    if "instagram.com/reel" not in url:
        update.message.reply_text("❌ Invalid link.")
        return

    try:
        media_id = cl.media_pk_from_url(url)
        media_info = cl.media_info(media_id)
        video_url = media_info.video_url

        update.message.reply_video(video_url, caption="✅ HD Reel")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_reel))
updater.start_polling()
updater.idle()
