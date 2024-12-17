# Food Recommendation and Personalized Banner Creation System

## Project Overview

This project implements a system that uses recommendation algorithms, LLM (Large Language Models), and DALL·E 3 to create personalized advertisement banners. The system consists of several key components:

1. **Recommendation System**: Uses user interaction data with products to provide personalized recommendations.
2. **LLM for Text Generation**: Creates individual product descriptions or offers tailored to users.
3. **DALL·E 3 for Image Creation**: Generates visual representations of recommended products based on text descriptions, and then creates advertisement banners that are overlaid onto the images.
4. **Personalized Banners**: Generated advertisement banners are added to images to grab users’ attention.

### Components Description

1. **Recommendation Algorithm**:
   The recommendation system is based on two approaches:
   - **Content-based Filtering**: The system analyzes products that a user has previously interacted with and suggests similar ones. It uses information about product categories and descriptions.
   - **Collaborative Filtering**: The system looks at interactions from other users with products and recommends items liked by similar users. The algorithm relies on an interaction matrix and uses Nearest Neighbors models to find similar preferences.

   This approach helps predict products that may appeal to the user based on their past behavior and the preferences of other users.

2. **LLM (Large Language Model)**:
   The system leverages models like **AI21**, **OpenAI**, or any other accessible LLM to generate personalized text descriptions based on product recommendations. These models take the cleaned product data and create engaging and unique descriptions, enhancing the user experience and increasing the effectiveness of marketing campaigns.

   The generated text is designed to be more attractive and aligned with user interests. For example: "While you're enjoying tasty apples with other fruits, we recommend complementing it with a delicious juice or light dessert."

3. **DALL·E 3 for Image Creation**:
   **DALL·E 3** is a powerful image generation model used to create visual representations of recommended products. The system generates an image based on a text prompt that describes the recommended items. DALL·E 3 creates an image of these products, which is then used for marketing and visual presentation purposes.

4. **Personalized Advertisement Banners**:
   After generating the image, a banner with personalized text is overlaid onto the image. The banner can contain recommendations, promotions, or other relevant messages. This feature ensures that users are presented with not only visual content but also engaging calls to action.

---

## How It Works

1. **Product Recommendations**: The system analyzes a user's interaction history with products (e.g., purchases, views, and items added to the cart) to suggest products they might be interested in.
   
2. **Text Generation with LLM**: Based on the recommendations, the LLM generates a personalized message that enhances the marketing appeal of the recommended products.

3. **Image Creation with DALL·E 3**: The generated text description is passed to the DALL·E 3 model, which creates an image depicting the recommended products.

4. **Adding Advertisement Banner**: A banner is overlaid on the generated image containing the personalized offer or recommendation.

5. **Saving the Result**: The final image is saved and can be used in promotional campaigns or displayed on websites.

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/food-recommendation-banner.git
    ```

2. Navigate to the project directory:

    ```bash
    cd food-recommendation-banner
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the necessary paths to data files and API keys as required.

---

## Usage

1. Make sure you have the following data files:
    - **user_interactions.csv**: Data on user interactions with products.
    - **final_standardized_labelled.csv**: Data on products with labels.
    - Ensure the files are placed in the correct folders.

2. Run the program:

    ```bash
    python main.py
    ```

3. The result will be an image with a banner overlaid, showcasing product recommendations.

---

## Project Structure

```
food-recommendation-banner/
│
├── Dataset_PSnake/
│   ├── user_interactions.csv
│   └── final_standardized_labelled.csv
│
├── app/
│   ├── banner.py
│   ├── image.py
│   ├── processing.py
│   └── __init__.py
│
├── config.py
├── llm/
│   └── ai21.py
├── recomender.py
└── main.py
```

- **Dataset_PSnake/** — Contains user and product data files.
- **app/** — Directory containing the functions for image processing, banner creation, and description cleaning.
- **llm/** — Interface for working with AI models like AI21 or OpenAI.
- **recomender.py** — File that contains the recommendation system logic.
- **main.py** — The main executable file that runs the entire process.

---

## Notes

- Ensure you have access to the required APIs for working with AI21, OpenAI, or other LLMs.
- The project uses libraries like `PIL` for image processing, `requests` for web services, and `scikit-learn` for recommendation algorithms.

---

## License

This project is licensed under the MIT License.
