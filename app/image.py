import requests
import os 
import hashlib
import logging
from config import settings
from llm.dalle3 import OpenAIImageGenerator

class ImageGenerator:
    def __init__(self):
        """Initialize the ImageGenerator with OpenAI image generation capabilities."""
        self.generator = OpenAIImageGenerator()
        os.makedirs(settings.DATA_PATH_GENERATED, exist_ok=True)
        self.logger = logging.getLogger(__name__)

    def generate_and_save(self, prompt: str) -> str:
        """
        Generate an image from a prompt and save it to disk.
        
        Args:
            prompt (str): The text prompt to generate the image from
            
        Returns:
            str: Path to the saved image file
            
        Raises:
            Exception: If image generation or saving fails
        """
        try:
            # Generate image using DALL-E
            response = self.generator.generate_image(prompt)
            image_url = response.data[0].url
            
            # Generate filename and full path
            image_name = self._generate_filename(prompt)
            image_path = os.path.join(settings.DATA_PATH_GENERATED , image_name)
            
            # Download and save the image
            self._download_image(image_url, image_path)
            
            self.logger.info(f"Image successfully saved to {image_path}")
            return image_path
            
        except Exception as e:
            self.logger.error(f"Failed to generate/save image: {str(e)}")
            raise

    def _download_image(self, image_url: str, save_path: str) -> None:
        """
        Download image from URL and save to disk.
        
        Args:
            image_url (str): URL of image to download
            save_path (str): Path where image should be saved
        """
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            
            with open(save_path, 'wb') as file:
                file.write(response.content)
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to download image: {str(e)}")
            raise
            
        except IOError as e:
            self.logger.error(f"Failed to save image: {str(e)}")
            raise

    def _generate_filename(self, prompt: str) -> str:
        """
        Generate a unique filename from the prompt.
        
        Args:
            prompt (str): Text prompt used to generate the image
            
        Returns:
            str: Generated filename with .png extension
        """
        hash_object = hashlib.md5(prompt.encode())
        short_name = hash_object.hexdigest()[:10]
        return f"{short_name}.png"
