from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Ciao! Sono un bot semplice 😊')

def help_command(update, context):
    update.message.reply_text('Scrivi /start per iniziare o mandami un messaggio!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    TOKEN = "8167300658:AAGl885SYrrZuOKAunHYsf4PRfeHqMA2PRQ"  # Metti qui il token del BotFather

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()