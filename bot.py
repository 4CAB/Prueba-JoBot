from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

import os

TOKEN = "<TOKEN_BOT>"
PORT = int(os.environ.get('PORT', '443'))

def start(update, context):
    update.message.reply_text('Hi!')

def main():
    bot = Bot(TOKEN)
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    # start webhook
    bot.delete_webhook()

    updater.start_webhook(listen="0.0.0.0",
                           port=PORT,
                           url_path=TOKEN,
                           webhook_url="https://chaqueta.herokuapp.com/webhook")
    updater.idle()

if __name__ == '__main__':
    print("Hello")
    main()