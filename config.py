import os  # Этот файл отвечает за загрузку настроек проекта
from dotenv import load_dotenv
load_dotenv()  # Загружаем переменные из файла .env
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Получаем токен бота из переменных окружения

if not BOT_TOKEN:  # Проверка: если токена нет -git status
    # останавливаем программу
    raise ValueError("BOT_TOKEN is not found in .env file")