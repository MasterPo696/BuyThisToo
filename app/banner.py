from PIL import Image, ImageDraw, ImageFont
import os
from app.colors import Colors, FONT_PATH

# Функция для добавления баннера на изображение
def make_banner_on_logo(image_path, text, banner_height_ratio=0.1, banner_width_ratio=0.8, font_size=20):
    # Открытие изображения
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Цвета текста и баннера
    text_color = Colors.WHITE
    banner_color = Colors.RED

    # Размеры изображения
    image_width, image_height = image.size

    # Размер баннера (по умолчанию, ширина баннера равна ширине изображения, а высота - процент от высоты)
    banner_height = int(image_height * banner_height_ratio)
    banner_width = int(image_width * banner_width_ratio)

    # Позиция баннера внизу изображения
    banner_x_start = (image_width - banner_width) // 2
    banner_y_start = image_height - banner_height

    # Нарисовать баннер (прямоугольник)
    draw.rectangle([banner_x_start, banner_y_start, banner_x_start + banner_width, banner_y_start + banner_height], fill=banner_color)

    # Загрузка шрифта с увеличенным размером
    font = ImageFont.load_default()
    try:
        font = ImageFont.truetype(FONT_PATH, size=font_size)  # Указываем путь к своему шрифту .ttf
    except IOError:
        font = ImageFont.load_default()  # Если шрифт не найден, используем стандартный

    # Разбиение текста на строки, если он не помещается
    max_text_width = int(banner_width * 0.8)  # Текст должен занимать не больше 80% ширины баннера
    lines = []
    words = text.split()
    current_line = ""
    
    # Перенос текста, если строка не помещается в заданную ширину
    for word in words:
        test_line = current_line + " " + word if current_line else word
        text_width, text_height = draw.textsize(test_line, font=font)
        
        if text_width <= max_text_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)  # Добавляем последнюю строку

    # Позиция для текста на баннере
    y_offset = banner_y_start + (banner_height - text_height * len(lines)) // 2
    for line in lines:
        text_width, text_height = draw.textsize(line, font=font)
        x_offset = (image_width - text_width) // 2  # Центрируем текст
        draw.text((x_offset, y_offset), line, fill=text_color, font=font)
        y_offset += text_height  # Смещаем y-координату для следующей строки

    # Путь к папке для сохранения
    save_folder = "/Users/masterpo/Desktop/BuyThisToo/data/pics/formated"

    # Извлекаем имя файла без расширения и формат
    base_name = os.path.splitext(os.path.basename(image_path))[0]  # Имя файла без расширения
    file_format = 'png'  # Вы можете установить нужный формат (например, 'jpg', 'png')

    # Формируем путь для сохранения с новым именем
    output_path = os.path.join(save_folder, f"{base_name}_modified.{file_format}")

    # Сохраняем изображение в новый файл
    image.save(output_path)

    print(f"Изображение сохранено как {output_path}")

