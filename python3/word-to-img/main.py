"""
word-to-img

將文字轉化成圖片
"""
import os
import string
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


INPUT_PATH = "input"
TARGET_PATH = "output"
if not os.path.exists(TARGET_PATH):
    os.mkdir(TARGET_PATH)


def draw_img(ch):
  img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("Hannotate.ttc", 80)
  draw.text((10, 0), ch, (0, 0, 0), font=font)
  img.save(TARGET_PATH + "/" + ch + ".png", "PNG")


if __name__ == "__main__":
  with open(INPUT_PATH, 'r') as file:
    content = file.read().translate(
        {ord(c): None for c in string.whitespace})
    for x in content:
      draw_img(x)
