from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")


def req(update, context):
    chat = update.effective_chat
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://innovations.kh.ua/wp-json/wp/v2/places'   
    r = requests.get(url,headers=headers)
    jsn = r.json()
    text = jsn[0]['acf']['adress'] +" " +jsn[0]['acf']['money']

    context.bot.send_message(chat_id=chat.id, text=text)


def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("req", req))
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
