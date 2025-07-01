from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

TOKEN = '7594237181:AAHwlqXJo43nP8q5qNc_HK505j-uGLhkERM'

def start(update, context):
    update.message.reply_text("👋 Welcome! Send me an Instagram Reel link to download.")

def handle_message(update, context):
    url = update.message.text
    if "instagram.com/reel" in url:
        update.message.reply_text("📥 Downloading reel...")

        api_url = "https://igram.io/api/ajaxSearch"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        data = f"q={url}"

        response = requests.post(api_url, data=data, headers=headers)

        if response.ok:
            try:
                json_data = response.json()
                video_url = json_data['data']['medias'][0]['url']
                update.message.reply_video(video_url)
            except:
                update.message.reply_text("⚠️ Couldn’t fetch video. Try another link.")
        else:
            update.message.reply_text("⚠️ Error reaching API. Try again later.")
    else:
        update.message.reply_text("❌ Please send a valid Instagram Reel link.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()