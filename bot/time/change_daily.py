#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


from datetime import time
import datetime

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Use hey')


def info(context: CallbackContext) -> None:
    job = context.job
    context.bot.send_message(job.context, text='Info')

def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def st(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(info, 1, context=chat_id, name=str(chat_id))


def daily(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    b = time(11, 45, 30)
    context.job_queue.run_daily(info, b, context=chat_id, name=str(chat_id))
    update.message.reply_text('daily')

def change_daily(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    b = time(int(context.args[0]), int(context.args[1]), int(context.args[2]))
    context.job_queue.run_daily(info, b, context=chat_id, name=str(chat_id))
    text = 'daily: '+ context.args[0] +' '+ context.args[1] +' '+ context.args[2]
    if job_removed:
        text += ' Old one was removed.'
    update.message.reply_text(text)


def chk(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    print(current_jobs[0].next_run_time)
    text = str(len(current_jobs))
    update.message.reply_text(text)



def stp(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Timer successfully cancelled!' if job_removed else 'You have no active timer.'
    update.message.reply_text(text)

def main() -> None:
    """Run bot."""
    updater = Updater("2034824924:AAFc0q0PYPezeZ6G5kE10uBWhWSurKks-8A")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("st", st))
    dispatcher.add_handler(CommandHandler("daily", daily))
    dispatcher.add_handler(CommandHandler("check", chk))
    dispatcher.add_handler(CommandHandler("stp", stp))    
    dispatcher.add_handler(CommandHandler("change_daily", change_daily))
    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()