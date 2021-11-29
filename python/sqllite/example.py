from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
import sqlite3
import datetime

def cat_list_value():
    if os.path.exists("categ_list.txt"):
        f = open('categ_list.txt','r')
        for line in f:
            string = line
        elements = string.split(' ')
        f.close()
        return elements
    else:
        return []

def total(update, context):
    conn = sqlite3.connect('finances.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM finances;")
    three_results = cur.fetchall()
    print(three_results)
    sum = 0
    for res in three_results:
        sum = sum+res[1]

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="total: "+str(sum))

def totaltime(update, context):
    conn = sqlite3.connect('finances.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM finances WHERE sumdate>'2021-11-29 11:56:59.401671';")
    three_results = cur.fetchall()
    print(three_results)
    sum = 0
    for res in three_results:
        sum = sum+res[1]

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="total: "+str(sum))

def costs_list(update, context):
    f = open('costs_list.txt','r')
    string = ''
    for line in f:
        string = string + line
    f.close()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string)

def start(update, context):
    conn = sqlite3.connect('finances.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS finances(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   sum INTEGER,
   cat VARCHAR(20),
   sumdate TIMESTAMP);
""")
    conn.commit()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")

def cat (update, context):
    f = open('categ_list.txt','r')
    for line in f:
        string = line
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string)

def addcat (update, context): #/addcat tech
    string = update.message.text
    elements = string.split(' ')
    f = open('categ_list.txt','r')
    for line in f:
        categories = line
    f.close
    f = open('categ_list.txt','w')
    f.write(categories)
    f.write(' '+elements[1])
    f.close()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Category "+elements[1]+" added.")


def costs(update, context):

    string = update.message.text
    elements = string.split(' ')
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])

def cost(update, context):
    string = update.message.text
    elements = string.split(' ')
    print( elements)
    conn = sqlite3.connect('finances.db')
    cur = conn.cursor()
    sql = f"INSERT INTO finances(sum, cat,sumdate) VALUES({-int (elements[2])}, '{elements[1]}','{datetime.datetime.now()}');"
    print(sql)
    cur.execute(sql)
    conn.commit()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=f"Get {int(elements[2])} costs in {elements[1]}")

def income(update, context):
    string = update.message.text
    elements = string.split(' ')
    print( elements)
    conn = sqlite3.connect('finances.db')
    cur = conn.cursor()
    sql = f"INSERT INTO finances(sum, cat, sumdate) VALUES({int (elements[2])}, '{elements[1]}','{datetime.datetime.now()}');"
    print(sql)
    cur.execute(sql)
    conn.commit()

def drop(update, context):  
    conn = sqlite3.connect('finances.db')
    cur = conn.cursor() 
    sql ="DROP table finances;"
    cur.execute(sql)
    conn.commit()

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler(cat_list_value(), costs))
dispatcher.add_handler(CommandHandler("cost", cost))
dispatcher.add_handler(CommandHandler("income", income))

dispatcher.add_handler(CommandHandler("cat", cat))
dispatcher.add_handler(CommandHandler("costs", costs_list))
dispatcher.add_handler(CommandHandler("total", total))
dispatcher.add_handler(CommandHandler("totaltime", totaltime))
dispatcher.add_handler(CommandHandler("drop", drop))

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
