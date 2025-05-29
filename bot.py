import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get("PORT", 8443))
HOST = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
WEBHOOK_PATH = f"/webhook/{TOKEN}"

def start(update, context):
    update.message.reply_text('Ciao! Sono un bot su Render con webhook!')

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

    if HOST:
        webhook_url = f"https://{HOST}{WEBHOOK_PATH}"
        # Stampa per debug
        print(f"Webhook impostato su {webhook_url}")
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=WEBHOOK_PATH.lstrip("/"),
        )
        updater.bot.set_webhook(webhook_url)
    else:
        updater.start_polling()
        print("Bot partito in modalità polling (locale)")

    updater.idle()

if __name__ == '__main__':
    main()