import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.environ["8167300658:AAGl885SYrrZuOKAunHYsf4PRfeHqMA2PRQ"]
PORT = int(os.environ.get("PORT", 8443))

def start(update, context):
    update.message.reply_text('Ciao! Sono un bot semplice 😊')

def help_command(update, context):
    update.message.reply_text('Scrivi /start per iniziare o mandami un messaggio!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Imposta il webhook
    HEROKU_APP_NAME = os.environ.get("provabot.onrender.com") or os.environ.get("HEROKU_APP_NAME")  # Render o Heroku
    if HEROKU_APP_NAME:
        # URL a cui Telegram manderà i messaggi
        webhook_url = f"https://{HEROKU_APP_NAME}/"
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
        )
        updater.bot.set_webhook(webhook_url + TOKEN)
    else:
        # fallback: polling (solo per sviluppo locale)
        updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()