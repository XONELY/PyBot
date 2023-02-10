import telebot
import random
from telebot import types

bot = telebot.TeleBot('6209692229:AAG8JZmSWr2XQ1dvhQ_AU3UNni4KC_mXGOk')
    


@bot.message_handler(commands=['start'])
def start(message):
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("🗿")
        btn1 = types.KeyboardButton("🧻")
        btn2 = types.KeyboardButton("✂️")

        markup.add(btn0,btn1,btn2)
        bot.send_message(message.from_user.id, "Привет! Давай сыграем в камень-ножницы-бумага")
        bot.send_message(message.from_user.id, "Твой ход:", reply_markup=markup)
        
 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    botStep = None
    playerStep = None
    win = None
    if message.text == "🗿":
         playerStep = 1
    elif message.text == "✂️":
        playerStep = 2
    elif message.text == "🧻":
        playerStep = 3
    else:
        bot.send_message(message.from_user.id, "Хммм, что-то не то..")

    botStep = random.randint(1,3)

    if botStep == 1:
        bot.send_message(message.from_user.id, "А я выбираю: 🗿")
    if botStep == 2:
        bot.send_message(message.from_user.id, "А я выбираю: ✂️")
    if botStep == 3:
        bot.send_message(message.from_user.id, "А я выбираю: 🧻") 


    
  
    if playerStep == botStep:
        win = 0
    if playerStep == 1 and botStep == 2:
        win = 1 
    if playerStep == 1 and botStep == 3:
        win = 2 
    if playerStep == 2 and botStep == 1:
        win = 2  
    if playerStep == 2 and botStep == 3:
        win = 1 
    if playerStep == 3 and botStep == 1:
        win = 1
    if playerStep == 3 and botStep == 2:
        win = 2
        

    if win == 0:
        bot.send_message(message.from_user.id, "Ничья! \n Давай еще раз!")
    if win == 1:
        bot.send_message(message.from_user.id, "Ты победил! \n Давай еще раз!")
    if win == 2:
        bot.send_message(message.from_user.id, "Я победил! \n Давай еще раз!")

bot.polling(none_stop=True, interval=0)