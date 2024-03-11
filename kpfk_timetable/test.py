import os
from dotenv import load_dotenv

# Завантаження змінних оточення з файлу .env в поточній робочій директорії
load_dotenv()

# Отримання значень змінних оточення
KEY = os.getenv('KEY')
NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

# Виведення отриманих значень
print("KEY:", KEY)
print("NAME:", NAME)
print("USER:", USER)
print("PASSWORD:", PASSWORD)
print("HOST:", HOST)
print("PORT:", PORT)
