from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

import random

msg = ["Бажаю щоб щастя зростало щогодини!", "Бажаю безмежної любові!", "У тебе все вийде якнайкраще!", "Рухаючись крок за кроком ти досягнеш мети", "Все буде супер!"]
img = ["https://mikh-maksi.github.io/probes/img/air.jpg", "https://mikh-maksi.github.io/probes/img/happy.jpg", "https://mikh-maksi.github.io/probes/img/happy2.jpg", "https://mikh-maksi.github.io/probes/img/flowers.jpg", "https://mikh-maksi.github.io/probes/img/morning.jpg"]

def key_buttons():
    kb = [[InlineKeyboardButton("Щаслива картка", callback_data="photo")],
    [InlineKeyboardButton("Щасливе повідомлення", callback_data="message")]]
    return kb

def start(update: Update, context: CallbackContext) -> None:
    keyboard = key_buttons()
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Оберіть один з варіантів:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    chat = update.effective_chat
    keyboard = key_buttons()
    reply_markup = InlineKeyboardMarkup(keyboard)

    if query.data == 'photo':
        photo_img = random.choice(img)
        context.bot.send_photo(chat_id=chat.id, photo=photo_img ,reply_markup=reply_markup)

    if query.data == 'message':
        text_msg = random.choice(msg)
        context.bot.send_message(chat_id=chat.id, text=text_msg, reply_markup=reply_markup)

def echo(update, context):
    global condition, account
    string_in = update.message.text



    keyboard = key_buttons()
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(string_out,reply_markup=reply_markup)



def main() -> None:
    updater = Updater("2136244102:AAEfZvt308Dh2bk58hSMmKIFwA3Ty-zq6bs")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
