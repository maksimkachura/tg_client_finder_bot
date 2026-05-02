from bot import bot  # Главный файл запуска бота

from database import init_db

# Обработчик команды / start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Бот работает 🚀')  # Отправляем сообщение пользователю

if __name__ == '__main__':  # Точка входа в программу
    print('Бот запущен!')
    init_db()
    bot.infinity_polling()  # Запускаем бота (он начинает слушать сообщения)

