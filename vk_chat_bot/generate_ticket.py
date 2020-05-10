from PIL import Image, ImageDraw, ImageFont
import requests
import io

TEMPLATE_PATH = ''
FONT_PATH = ''
FONT_SIZE = 20
AVATAR_SIZE = 80
AVATAR_OFFSET = (50, 190)

def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    draw = ImageDraw.Draw(base)
    draw.text((200, 195), name, font=font, fill=(0, 0, 0, 255))
    draw.text((200, 230), email, font=font, fill=(0, 0, 0, 255))
    response = requests.get(url=f'https://api.adorable.io/avatars/{AVATAR_SIZE}/{email}')
    avatar_file = io.BytesIO(response.content)
    avatar = Image.open(avatar_file)
    base.paste(avatar, AVATAR_OFFSET)
    temp_file = io.BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file