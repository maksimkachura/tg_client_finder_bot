#создаeм базу данных и таблицу users

import sqlite3  # библиотека для работы с SQLite

from pathlib import Path  # для сборки путя к файлу базы

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "bot.db"  # путь к базе данных

def init_db():  # функция для создания базы и таблицы
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                username TEXT,
                first_name TEXT
            )
        """)
        conn.commit()