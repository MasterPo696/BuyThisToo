from PIL import Image, ImageDraw, ImageFont
import requests
from config import SYSTEM_MESSAGE2, DESCRIPTION
from llm.ai21 import LLMServiceAI21
from app.image import generate_save_image
from app.proccessing import clean_food_description
from app.banner import make_banner_on_logo
import re
from recomender import Recommender

prompt = 'tasty and healthy apples with other fruits'

RESPONSE = """Hey there, Productivity Pro! Looks like you're gearing up for some serious snack attacks and poolside adventures! While you're keeping your hands protected and your taste buds happy, why not dive into "Atomic Habits" by James Clear for some productivity hacks, or unwind with the hilarious "The Hitchhiker's Guide to the Galaxy" by Douglas Adams? And for those moments when you need a break, let "Guardians of the Galaxy" soundtrack be your background music. Enjoy!"""

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

    response = model.generate_response(SYSTEM_MESSAGE2, user_message=cleaned_description)

    image_path = generate_save_image(IMAGE_PROMPT + cleaned_description)

    # image_path = "/Users/masterpo/Desktop/BuyThisToo/data/pics/generated/tasty_and_healthy_apples_with_other_fruits.png"
    make_banner_on_logo(image_path, RESPONSE,  banner_height_ratio=0.1, banner_width_ratio=0.8)
    

# Запуск программы
if __name__ == "__main__":
    main()
