import base64
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
import PIL.Image
import requests



def create_image_tobase(text):
    img = Image.new('RGB', (640, 360), color=(255, 255, 255))
    fnt = ImageFont.truetype('/Library/Fonts/Helvetica Neue UltraLight.ttf', 280)
    d = ImageDraw.Draw(img)
    d.text((15, 15), str(text), font=fnt, fill=(0, 0, 0))
    img.save('pil_text_font.png')
    image = open('pil_text_font.png', 'rb')
    image_read = image.read()
    image_encode = base64.b64encode(image_read)
    image_encode = str(image_encode).replace("b'","")
    image_encode = str(image_encode).replace("'", "")
    return image_encode
a = create_image_tobase("0079")
print(a)