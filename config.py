import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API keys
    AI21_API_KEY = os.getenv("AI21_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Data paths
    DATA_PATH = os.getenv("DATA_PATH")
    DATA_PATH_GENERATED = os.getenv("DATA_PATH_GENERATED")

    # System messages
    SYSTEM_MESSAGE = os.getenv("SYSTEM_MESSAGE")
    SYSTEM_MESSAGE2 = os.getenv("SYSTEM_MESSAGE2")
    EXAMPLE_DESCRIPTION = os.getenv("EXAMPLE_DESCRIPTION")

settings = Settings()