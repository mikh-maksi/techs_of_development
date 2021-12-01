from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

import random

img = ["https://mikh-maksi.github.io/probes/img/air.jpg", "https://mikh-maksi.github.io/probes/img/happy.jpg", "https://mikh-maksi.github.io/probes/img/happy2.jpg", "https://mikh-maksi.github.io/probes/img/flowers.jpg", "https://mikh-maksi.github.io/probes/img/morning.jpg"]

def start(update: Update, context: CallbackContext) -> None:
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Щаслива картка", callback_data="photo")]])
    update.message.reply_text('Оберіть щастя:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    chat = update.effective_chat
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Щаслива картка", callback_data="photo")]])

    if query.data == 'photo':
        photo_img = random.choice(img)
        context.bot.send_photo(chat_id=chat.id, photo=photo_img ,reply_markup=reply_markup)

def main() -> None:
    updater = Updater("")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))


    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
