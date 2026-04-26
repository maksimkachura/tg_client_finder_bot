from bot import bot

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Бот работает 🚀')

if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()

