# Технологии разработки
Цель данного курса - познакомить студентов с основными распространенными на сегодня технологиями и расширить их навыки в сфере разработки в одной из технологий.
**Обзорная часть курса:** 
1. *Жизненный цикл разработки ПО. Основные роли.*
2. *Технологии создания продукта: боли/выгоды - болеутолители/создатели выгод.*
3. *Web-стек разработки ПО. Домены, хостинг, сайт. Создание сайта на WP. Использование плагинов. Корректировки HTML+CSS.*
4. *Разработка Телеграм-ботов.*
5. _Бек-енд. Создание оболочки по настройке ботов. Связь бек-енда и фронтенда._
6. _Работа с БД на MySQL_
7. Парсинг.
8. Создание продукта: информацинный прдукт с парсингом данных и раздачей информации.

## Исходные коды
* [Эхо-бот](https://github.com/mikh-maksi/own-finances-bot/blob/main/step02/02bot_echo.py)

> "Все - получится, если делать"

```python
from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    print(update.message.text)
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
```
## Рекомендации пользователям

## Инструкции для разработчиков

![Технологии разработки ПО](https://github.com/mikh-maksi/techs_of_development/blob/main/tech-planet.jpg)
