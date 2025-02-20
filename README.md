# 🍽️ Food Recommendation and Personalized Banner Creation System

## 🌟 Project Overview

This innovative system combines recommendation algorithms, LLM (Large Language Models), and DALL·E 3 to create personalized advertisement banners. The system features:

🔍 **Recommendation System**: Analyzes user interaction data for personalized product suggestions
🤖 **LLM for Text Generation**: Creates tailored product descriptions and offers
🎨 **DALL·E 3 for Image Creation**: Generates visual product representations
🎯 **Personalized Banners**: Adds eye-catching advertisement banners to images

### 🛠️ Components Description

#### 1. 📊 Recommendation Algorithm
Two powerful approaches:
- **Content-based Filtering**: Analyzes user's previous interactions
- **Collaborative Filtering**: Uses similar users' preferences via Nearest Neighbors models

#### 2. 🧠 LLM (Large Language Model)
Leverages models like **AI21** and **OpenAI** to generate engaging descriptions. Example:
> "While you're enjoying tasty apples with other fruits, we recommend complementing it with a delicious juice or light dessert."

#### 3. 🎨 DALL·E 3 Integration
Creates stunning visual representations based on text prompts for marketing purposes.

#### 4. 🎯 Personalized Advertisement Banners
Overlays customized banners with recommendations and promotions on generated images.

## ⚙️ How It Works

1. 📊 **Product Recommendations**: Analyzes user history
2. ✍️ **Text Generation**: Creates personalized marketing messages
3. 🖼️ **Image Creation**: Generates product visuals with DALL·E 3
4. 🎨 **Banner Addition**: Overlays personalized offers
5. 💾 **Result Saving**: Stores final images for campaigns

## 🚀 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MasterPo696/BuyThisToo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd BuyThisToo
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the necessary paths to data files and API keys as required.

## 📋 Usage

1. Make sure you have the following data files:
    - **user_interactions.csv**: Data on user interactions with products.
    - **final_standardized_labelled.csv**: Data on products with labels.
    - Ensure the files are placed in the correct folders.

2. Run the program:

    ```bash
    python main.py
    ```

3. The result will be an image with a banner overlaid, showcasing product recommendations.

## 📁 Project Structure

```
BuyThisToo/
│
├── data/
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

- **data/** — Contains user and product data files.
- **app/** — Directory containing the functions for image processing, banner creation, and description cleaning.
- **llm/** — Interface for working with AI models like AI21 or OpenAI.
- **recomender.py** — File that contains the recommendation system logic.
- **main.py** — The main executable file that runs the entire process.

## 📝 Notes

- 🔑 Ensure API access for AI21, OpenAI, or other LLMs.
- 📚 Required libraries:
  - `PIL` for image processing
  - `requests` for web services
  - `scikit-learn` for recommendation algorithms

## 📄 License

This project is licensed under the MIT License.

---
Made with ❤️ for food recommendation and marketing automation
