from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
def read_reg():
    f = open('E:\max\\bot\\reg.txt', 'r')
    for line in f:
            elements=line.split(";")
    f.close
    return elements

def create_keyboard():
    dicts = []
    elem = read_reg()
    dict1 = dict(descr='Введите имя', cd_data='name')
    dicts.append(dict1)
    dict2 = dict(descr='Кол-во сотрудников', cd_data='n')
    dicts.append(dict2)
    dict3 = dict(descr='Сфера деятельности', cd_data='kved')
    dicts.append(dict3)
    dict4 = dict(descr='Пройти тест', cd_data='test')
    dicts.append(dict4)

    print(dicts)

    # keyboard = [
    #     [InlineKeyboardButton("Введите имя", callback_data='name'),InlineKeyboardButton("Кол-во сотрудников", callback_data='22'),],
    #     [InlineKeyboardButton("Сфера деятельности", callback_data='44')],
    # ]
    keyboards = []
    keyboard = []
    for i in range(len(elem)):
        if elem[i] =='':
            keyboard.append(InlineKeyboardButton(dicts[i].get('descr'),callback_data=dicts[i].get('cd_data')))
    keyboards.append(keyboard)
    return keyboards
print(create_keyboard())
