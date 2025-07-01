import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "7594237181:AAHwlqXJo43nP8q5qNc_HK505j-uGLhkERM"

def start(update, context):
    update.message.reply_text("👋 Send any Instagram Reel link to download in Full HD.")

def download_reel(update, context):
    url = update.message.text.strip()
    
    if "instagram.com/reel" not in url:
        update.message.reply_text("❌ Please send a valid Instagram Reel URL.")
        return

    update.message.reply_text("📥 Downloading... Please wait.")

    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0"
        }
        data = f"url={url}"
        res = requests.post("https://snapsave.app/action.php", data=data, headers=headers)
        
        # Extract video link from response HTML (ugly but works)
        video_url = res.text.split('href="')[1].split('"')[0]

        update.message.reply_video(video_url, caption="✅ Reel in Full HD")

    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_reel))
updater.start_polling()
updater.idle()
