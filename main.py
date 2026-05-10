from bot import bot  # Главный файл запуска бота

from database import init_db, add_user

# Обработчик команды / start
@bot.message_handler(commands=['start'])
def send_welcome(message):

    telegram_id = message.from_user.id  # Берём ID
    user_name = message.from_user.username  # Берём username
    first_name = message.from_user.first_name  # Берём имя
    add_user(telegram_id, user_name, first_name)

    bot.send_message(message.chat.id, 'Бот работает 🚀')  # Отправляем сообщение пользователю

if __name__ == '__main__':  # Точка входа в программу
    print('Бот запущен!')
    init_db()
    bot.infinity_polling()  # Запускаем бота (он начинает слушать сообщения)

