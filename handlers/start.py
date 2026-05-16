from bot import bot

from database import add_user

# Обработчик команды / start
@bot.message_handler(commands=['start'])
def send_welcome(message):

    telegram_id = message.from_user.id  # Берём ID
    user_name = message.from_user.username  # Берём username
    first_name = message.from_user.first_name  # Берём имя
    add_user(telegram_id, user_name, first_name)

    bot.send_message(message.chat.id, 'Бот работает 🚀')  # Отправляем сообщение пользователю