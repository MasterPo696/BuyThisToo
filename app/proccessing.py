import re
from config import settings


class FoodDescriptionCleaner:
    """A class for cleaning food descriptions by removing measurements and quantities."""
    
    def __init__(self):
        # Regular expression pattern to match numbers and units of measurement
        self.measurement_pattern = r'\d+(\s?[a-zA-Z]+|\s?g|ml|G|pieces|x|cm|grams|flavour|\&nbsp;)'

    def clean_description(self, description_list):
        cleaned_list = []
        
        # Process each sublist of descriptions
        for item_list in description_list:
            cleaned_items = []
            for food_item in item_list:
                # Remove measurements and clean whitespace
                cleaned_food = re.sub(self.measurement_pattern, '', food_item)
                cleaned_items.append(cleaned_food.strip())
            cleaned_list.append(cleaned_items)

        # Concatenate all cleaned descriptions
        cleaned_text = ""
        for i in range(len(description_list)):
            for j in range(len(description_list[i])):
                cleaned_text += description_list[i][j]
                
        return cleaned_text
