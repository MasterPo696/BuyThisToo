import requests
import os 
from config import DATA_PATH
from llm.dalle3 import OpenAIImageGenerator
from config import NEW_KEY
import hashlib

def generate_save_image(prompt):
    # Создаём папку 'pics', если она не существует
    os.makedirs(DATA_PATH, exist_ok=True)

    # Инициализируем класс генератора изображений
    generator = OpenAIImageGenerator(api_key=NEW_KEY)

    # Генерируем изображение
    response = generator.generate_image(prompt)

    # URL сгенерированного изображения
    image_url = response.data[0].url

    # Генерация имени файла
    image_name = generate_image_name(prompt)

    # Полный путь для сохранения изображения
    image_path = os.path.join(DATA_PATH, image_name)

    # Скачиваем и сохраняем изображение
    download_image(image_url, image_path)

    print(f"Изображение сохранено как {image_path}")

    return image_path

def download_image(image_url, save_path):
    """Скачивает изображение по URL и сохраняет его на диск."""
    image_data = requests.get(image_url).content
    with open(save_path, 'wb') as file:
        file.write(image_data)

# Функция для генерации короткого имени файла из текста
def generate_image_name(prompt):
    """Генерирует короткое имя файла из текста запроса, ограниченное 10 символами."""
    
    # Используем хеширование для генерации уникального имени
    hash_object = hashlib.md5(prompt.encode())  # Преобразуем строку в байты и хешируем
    short_name = hash_object.hexdigest()[:10]  # Берём только первые 10 символов хеша
    
    return f"{short_name}.png"
