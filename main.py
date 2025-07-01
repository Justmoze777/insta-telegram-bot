import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "7594237181:AAHwlqXJo43nP8q5qNc_HK505j-uGLhkERM"

def start(update, context):
    update.message.reply_text("👋 Send me any Instagram Reel link to download in HD.")

def download_reel(update, context):
    url = update.message.text.strip()
    
    if "instagram.com/reel" not in url:
        update.message.reply_text("❌ Please send a valid Instagram Reel URL.")
        return

    update.message.reply_text("📥 Downloading Full HD reel...")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0',
        }
        response = requests.post(
            "https://saveig.app/api/ajaxSearch",
            headers=headers,
            data={"q": url}
        )
        data = response.json()

        if "data" in data and data["data"]["medias"]:
            video_url = data["data"]["medias"][0]["url"]
            update.message.reply_video(video_url, caption="✅ Reel downloaded in HD.")
        else:
            update.message.reply_text("⚠️ Couldn't fetch video. Try a different link.")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_reel))
updater.start_polling()
updater.idle()
