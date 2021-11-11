import logging
import random
from read_regs import read_reg, create_keyboard

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


logger = logging.getLogger(__name__)

places = ["https://innovations.kh.ua/ucan","https://innovations.kh.ua/ucan1","https://innovations.kh.ua/ucan2"]
links_list = []

def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    f = open('E:\max\\bot\links.txt', 'r')
    for line in f:
        links_list.append(line)
    f.close

    f = open('E:\max\\bot\\reg.txt', 'r')
    for line in f:
        elements=line.split(";")
    f.close

    # keyboard = [
    #     [InlineKeyboardButton("Введите имя", callback_data='name'),InlineKeyboardButton("Кол-во сотрудников", callback_data='22'),],
    #     [InlineKeyboardButton("Сфера деятельности", callback_data='44')],
    # ]
    keyboard = create_keyboard()
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите сферу:', reply_markup=reply_markup)

def reg(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Р1", callback_data='r11'),InlineKeyboardButton("P2", callback_data='r22'),InlineKeyboardButton("Р3", callback_data='r33'),],
        [InlineKeyboardButton("Р4", callback_data='r44')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Кто Вы?:', reply_markup=reply_markup)

def links(update: Update, context: CallbackContext) -> None:
    string = random.choice(links_list)
    update.message.reply_text(string)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    accept = [[InlineKeyboardButton("Принять", callback_data='1'),InlineKeyboardButton("Отказаться", callback_data='2'),InlineKeyboardButton("Еще", callback_data='3')],]
    reply_markup_accept = InlineKeyboardMarkup(accept)



    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    print(query.data)

    if query.data == '11':
        string = random.choice(places)
        query.edit_message_text(text=string, reply_markup=reply_markup_accept)
    elif query.data == '22':
        string = random.choice(places)
        query.edit_message_text(text=string, reply_markup=reply_markup_accept)
    elif query.data == '33':
        string = random.choice(places)
        query.edit_message_text(text=string, reply_markup=reply_markup_accept)
    if query.data == 'name':
        chat = update.effective_chat
        f = open('reg.txt', 'a')
        f_string = chat.id
        f.write(f"{f_string};1\n")
        f.close

        string = "You have been registered"
        query.edit_message_text(text=string)

    if query.data == 'r11':
        chat = update.effective_chat
        f = open('reg.txt', 'a')
        f_string = chat.id
        f.write(f"{f_string};1\n")
        f.close

        string = "You have been registered"
        query.edit_message_text(text=string)
    elif query.data == 'r22':
        chat = update.effective_chat
        f = open('reg.txt', 'a')
        f_string = chat.id
        f.write(f"{f_string};2\n")
        f.close
        string = "You have been registered"
        query.edit_message_text(text=string)
    elif query.data == 'r33':
        chat = update.effective_chat
        f = open('reg.txt', 'a')
        f_string = chat.id
        f.write(f"{f_string};3\n")
        f.close
        string = "You have been registered"
        query.edit_message_text(text=string)
    elif query.data == 'r44':
        chat = update.effective_chat
        f = open('reg.txt', 'a')
        f_string = chat.id
        f.write(f"{f_string};4\n")
        f.close
        string = "You have been registered"
        query.edit_message_text(text=string)
    else:
        query.edit_message_text(text=f"Ссылка на оплату")

def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2034824924:AAFc0q0PYPezeZ6G5kE10uBWhWSurKks-8A")

    updater.dispatcher.add_handler(CommandHandler('links', links))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('reg', reg))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
