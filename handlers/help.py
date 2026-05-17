from bot import bot  # импортируем объект бота из файла bot.py


@bot.message_handler(commands=['help'])

def send_help(message):
    bot.send_message(
        message.chat.id,
        'Доступные команды:\n'
        '/start — запустить бота\n'
        '/help — показать помощь'
    )
