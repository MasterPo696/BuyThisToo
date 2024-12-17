import requests
import logging
from config import AI21_API_KEY



import logging
# from ai21 import AI21Client
from config import AI21_API_KEY
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_ai21.chat_models import ChatAI21

class LLMServiceAI21:
    def __init__(self):
        """Инициализация AI21 модели."""
        try:
            self.parser = StrOutputParser()
            self.model = ChatAI21(model="jamba-instruct", api_key=AI21_API_KEY, streaming=True)
        except Exception as e:
            logging.error(f"Ошибка инициализации AI21: {e}")
            self.model = None

    def generate_response(self, system_message, user_message):
        """Генерирует ответ на основе системного и пользовательского сообщения."""
        if not self.model:
            logging.error("Модель AI21 не инициализирована.")
            return None
        
        try:
            messages = [
                SystemMessage(content=system_message),
                HumanMessage(content=user_message)
            ]
            response = self.model.invoke(messages)
            return self.parser.invoke(response)
        except Exception as e:
            logging.error(f"Ошибка при генерации ответа AI21: {e}")
            return "[Ошибка: Не удалось получить ответ от ИИ.]"





