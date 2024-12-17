from openai import OpenAI

# Класс для работы с OpenAI API
class OpenAIImageGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_image(self, prompt, model="dall-e-3", size="1024x1024", n=1):
        """Генерирует изображение по запросу."""
        response = self.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality="standard",
            n=n
        )
        return response
