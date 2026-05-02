import telebot  # Здесь создаётся объект бота, через который мы будем работать с Telegram
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)  # Создаем бота с помощью токена