import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bs4 import BeautifulSoup

TOKEN = "7594237181:AAHwlqXJo43nP8q5qNc_HK505j-uGLhkERM"

def start(update, context):
    update.message.reply_text("👋 Send me any Instagram Reel link to download in Full HD.")

def download_reel(update, context):
    url = update.message.text.strip()
    
    if "instagram.com/reel" not in url:
        update.message.reply_text("❌ Please send a valid Instagram Reel URL.")
        return

    update.message.reply_text("📥 Downloading... Please wait.")

    try:
        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        data = {
            'id': url,
            'locale': 'en'
        }

        res = session.post("https://ssstik.io/abc", headers=headers, data=data)
        soup = BeautifulSoup(res.text, "html.parser")

        video_tag = soup.find("a")
        if video_tag and video_tag.get("href"):
            video_url = video_tag["href"]
            update.message.reply_video(video_url, caption="✅ Full HD Reel")
        else:
            update.message.reply_text("⚠️ Video not found. Try another link or make sure it's public.")

    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_reel))
updater.start_polling()
updater.idle()
