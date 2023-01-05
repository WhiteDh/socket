import telebot
from config import *
from telebot import types
bot = telebot.TeleBot(TELEGRAM_BOT_API, parse_mode="HTML")


@bot.message_handler(commands=['start', 'help'])
def phone (message):
    print(message.from_user.first_name)
    print(message)
    keyboard = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True)
    button_phone = types.KeyboardButton (text ="send number",request_contact = True)
    keyboard.add (button_phone)
    bot.send_message (message.chat.id, 'Phone number', reply_markup = keyboard)

@bot.message_handler()
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
