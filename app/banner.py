from PIL import Image, ImageDraw, ImageFont
import os
from app.colors import Colors, FONT_PATH

class Banner:
    def __init__(self, image_path, text, banner_height_ratio=0.1, banner_width_ratio=0.8, font_size=20):
        self.image_path = image_path
        self.text = text
        self.banner_height_ratio = banner_height_ratio
        self.banner_width_ratio = banner_width_ratio
        self.font_size = font_size
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)
        self.image_width, self.image_height = self.image.size
        self.text_color = Colors.WHITE
        self.banner_color = Colors.RED
        self.font = self._load_font()
        
    def _load_font(self):
        """Load font file or fallback to default"""
        try:
            return ImageFont.truetype(FONT_PATH, size=self.font_size)
        except IOError:
            return ImageFont.load_default()

    def _calculate_banner_dimensions(self):
        """Calculate banner dimensions based on ratios"""
        banner_height = int(self.image_height * self.banner_height_ratio)
        banner_width = int(self.image_width * self.banner_width_ratio)
        banner_x_start = (self.image_width - banner_width) // 2
        banner_y_start = self.image_height - banner_height
        return banner_width, banner_height, banner_x_start, banner_y_start

    def _split_text_into_lines(self, max_width):
        """Split text into lines that fit within max_width"""
        lines = []
        words = self.text.split()
        current_line = ""
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            text_width, _ = self.draw.textsize(test_line, font=self.font)
            
            if text_width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
                
        lines.append(current_line)
        return lines

    def _draw_banner(self):
        """Draw the banner rectangle"""
        banner_width, banner_height, x_start, y_start = self._calculate_banner_dimensions()
        self.draw.rectangle(
            [x_start, y_start, x_start + banner_width, y_start + banner_height],
            fill=self.banner_color
        )
        return banner_width, banner_height, x_start, y_start

    def _draw_text(self, banner_width, banner_height, banner_x_start, banner_y_start):
        """Draw text on the banner"""
        max_text_width = int(banner_width * 0.8)
        lines = self._split_text_into_lines(max_text_width)
        
        _, text_height = self.draw.textsize("Test", font=self.font)
        y_offset = banner_y_start + (banner_height - text_height * len(lines)) // 2
        
        for line in lines:
            text_width, text_height = self.draw.textsize(line, font=self.font)
            x_offset = (self.image_width - text_width) // 2
            self.draw.text((x_offset, y_offset), line, fill=self.text_color, font=self.font)
            y_offset += text_height

    def save(self):
        """Save the modified image"""
        save_folder = "/Users/masterpo/Desktop/BuyThisToo/data/pics/formated"
        base_name = os.path.splitext(os.path.basename(self.image_path))[0]
        output_path = os.path.join(save_folder, f"{base_name}_modified.png")
        self.image.save(output_path)
        print(f"Image saved as {output_path}")
        return output_path

    def create(self):
        """Create banner with text"""
        banner_dims = self._draw_banner()
        self._draw_text(*banner_dims)
        return self.save()


def make_banner_on_logo(image_path, text, banner_height_ratio=0.1, banner_width_ratio=0.8, font_size=20):
    banner = Banner(image_path, text, banner_height_ratio, banner_width_ratio, font_size)
    return banner.create()
