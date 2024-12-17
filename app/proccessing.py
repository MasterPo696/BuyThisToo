import re
from config import DESCRIPTION
# Регулярное выражение для удаления чисел и единиц измерения (например, "100 pieces", "70 gm", "170ml", "150G")
def clean_food_description(DESCRIPTION):
    cleaned_list = []
    for item in DESCRIPTION:
        cleaned_item = []
        for food in item:
            # Убираем все цифры и единицы измерения, оставляем только название продукта
            cleaned_food = re.sub(r'\d+(\s?[a-zA-Z]+|\s?g|ml|G|pieces|x|cm|grams|flavour|\&nbsp;)', '', food)
            cleaned_item.append(cleaned_food.strip())  # Убираем лишние пробелы
        cleaned_list.append(cleaned_item)

    cleaned_text = ""

    for x in range(len(DESCRIPTION)):
        for i in range(len(DESCRIPTION[x])):
            cleaned_text += DESCRIPTION[x][i]
            
    return cleaned_text



