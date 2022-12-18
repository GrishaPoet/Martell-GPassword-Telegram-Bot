import telebot 
import config
from telebot import types
import spisok
import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFHGIJKLNOPQRSTUVWXYZ'

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='''👋 Привет! Я — Martell, робот, созданный человеком. 
Я умею генирировать универсальные пароли для ваших учётных записей. Также могу дать пару советов по информационной безопасности.''')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🚀 Генерация пароля")
    btn2 = types.KeyboardButton("❓ Информация")
    btn3 = types.KeyboardButton("🌐 Советы по ИБ")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text='''Пожалуйста, воспользуйтесь кнопками, чтобы начать пользоваться функциями Martell.''', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def buttons(message):
    if(message.text == "🚀 Генерация пароля"):
        password = ''
        for i in range(15):
            password += random.choice(chars)
        bot.send_message(message.chat.id, text=(f'''Ваш сгенирированный пароль: {password}'''))
        
    elif(message.text == "❓ Информация"):
        bot.send_message(message.chat.id, text=f'''⚙️ Martell — робот, который преднозначен для генерации универсальных паролей для ваших учётных записей.
⚠️ Мы не сохраняем и не храним сгенерированные пароли, ваши переписки с чат-ботом и другие какие-либо данные. Также мы не несём ответственность за все возможные утечки или взломы.''')
    

    elif(message.text == "🌐 Советы по ИБ"):
        b = random.choice(spisok.sp)
        b1 = b['advice']
        b2 = b['title']
        bot.send_message(message.chat.id, text=f'''{b1}\n
{b2}''')


            
bot.polling(none_stop=True)