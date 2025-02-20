import logging
import openai
from config import settings

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

class LLMServiceOpenAI:
    def __init__(self, max_tokens=150):

        try:
            self.parser = StrOutputParser()
            openai.api_key = settings.OPENAI_API_KEY
            self.max_tokens = max_tokens
        except Exception as e:
            logging.error(f"Ошибка инициализации OpenAI: {e}")

    def generate_response(self, system_message, user_message):
        try:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=messages,
                max_tokens=self.max_tokens
            )
            return self.parser.invoke(response['choices'][0]['message']['content'])
        except Exception as e:
            logging.error(f"Ошибка при генерации ответа OpenAI: {e}")
            return "[Ошибка: Не удалось получить ответ от ИИ.]"
