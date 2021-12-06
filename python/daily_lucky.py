from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import random

from datetime import time
import datetime

def start(update: Update, context: CallbackContext) -> None:
    b = time(7, 00, 00)
    chat_id = update.message.chat_id
    context.job_queue.run_daily(lucky_message, b, context=chat_id, name=str(chat_id))
    update.message.reply_text('Lucky message on 09:00')

def lucky_message(context: CallbackContext) -> None:
    job = context.job
    msg = ["Бажаю щоб щастя зростало щогодини!", "Бажаю безмежної любові!", "У тебе все вийде якнайкраще!", "Рухаючись крок за кроком ти досягнеш мети", "Все буде супер!"]
    string_out = random.choice(msg)
    context.bot.send_message(job.context, text=string_out)

def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

def st(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(lucky_message, 1, context=chat_id, name=str(chat_id))

def changedaily(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    string = update.message.text
    elements = string.split(' ')
    h = int(elements[1])
    m = int(elements[2])
    s = int(elements[3])
    b = time(h-2, m, s)
    context.job_queue.run_daily(lucky_message, b, context=chat_id, name=str(chat_id))
    update.message.reply_text(f"Change daily message for {h}:{m}:{s}")



def stp(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    
    text = 'Timer successfully cancelled!' if job_removed else 'You have no active timer.'
    update.message.reply_text(text)

def main() -> None:
    """Run bot."""
    updater = Updater("2136244102:AAEfZvt308Dh2bk58hSMmKIFwA3Ty-zq6bs")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("st", st))
    dispatcher.add_handler(CommandHandler("changedaily", changedaily))
    dispatcher.add_handler(CommandHandler("stp", stp))
    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
