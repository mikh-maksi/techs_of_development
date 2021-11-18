import schedule
import time


from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def job():
    print("I'm working...")

def job_m():
    print("Minute...")
    global_context.bot.send_message(chat_id=global_id, text="Hey!")
    # chat = update.effective_chat
    # context.bot.send_message(chat_id=chat.id, text=str(total_dict))

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("23:00").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":10").do(job_m)
schedule.every().minute.at(":20").do(job_m)
schedule.every().minute.at(":30").do(job_m)
schedule.every().minute.at(":40").do(job_m)
schedule.every().minute.at(":50").do(job_m)
schedule.every().minute.at(":00").do(job_m)


global_update = ''
global_context = ''
global_id = ''


def start(update, context):
    global global_update,global_context,global_id
    global_update = update
    global_context = context
    string_out = "Start"
    chat = update.effective_chat
    global_id = chat.id
    context.bot.send_message(chat_id=chat.id, text="Start")
    update.message.reply_text(string_out)

def echo(update, context):
    string_in = update.message.text
    string_out = string_in
    update.message.reply_text(string_out)

def hey(update, context):
     global_context.bot.send_message(chat_id=global_id, text="Hey!")

updater = Updater("2013484013:AAGNF0KtAimfPfyLR2yPZs-JYsJNv7sFRwA")

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("hey", hey))
dispatcher.add_handler(MessageHandler(Filters.all, echo))



updater.start_polling()
updater.idle()

while True:
    schedule.run_pending()
    time.sleep(1)