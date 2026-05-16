from bot import bot  # Главный файл запуска бота

from database import init_db

import handlers.start

if __name__ == '__main__':  # Точка входа в программу
    print('Бот запущен!')
    init_db()
    bot.infinity_polling()  # Запускаем бота (он начинает слушать сообщения)

