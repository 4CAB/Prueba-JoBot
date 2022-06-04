from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

import os

TOKEN = "5231646387:AAG1qWow9zgkit_TWtEV1Q_zEPdw7dBIVvw"
PORT = int(os.environ.get('PORT', '8443'))
# handlers
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def main():
    # add dispatcher
    bot = Bot(TOKEN)
    updater = Updater(TOKEN)
    # add handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    # start webhook
    bot.delete_webhook()

    updater.start_webhook(listen="0.0.0.0",
                           port=PORT,
                           url_path=TOKEN,
                           webhook_url="https://webjook.herokuapp.com/" + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()