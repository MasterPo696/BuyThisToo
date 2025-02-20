from PIL import Image, ImageDraw, ImageFont
import requests
from config import settings
from llm.ai21 import LLMServiceAI21
from app.image import generate_save_image
from app.proccessing import clean_food_description
from app.banner import make_banner_on_logo
import re
from app.recomender import Recommender




IMAGE_PROMPT = "Put all these food in one picture as add banner"

# Главная функция для создания и сохранения изображения
def main():

    user_id = 6633

    model = LLMServiceAI21()
    recommender = Recommender(
        interactions_path="Dataset_PSnake/user_interactions.csv",
        products_path="Dataset_PSnake/final_standardized_labelled.csv"
    )
    
    cleaned_description = clean_food_description(recommender.recommend(user_id))

    response = model.generate_response(settings.SYSTEM_MESSAGE2, user_message=cleaned_description)

    image_path = generate_save_image(IMAGE_PROMPT + cleaned_description)

    # image_path = "/Users/masterpo/Desktop/BuyThisToo/data/pics/generated/tasty_and_healthy_apples_with_other_fruits.png"
    make_banner_on_logo(image_path, response,  banner_height_ratio=0.1, banner_width_ratio=0.8)
    

# Запуск программы
if __name__ == "__main__":
    main()
