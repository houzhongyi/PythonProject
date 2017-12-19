#coding:utf-8
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

img = Image.new("RGB", (250,100), (255,0,255))

draw = ImageDraw.Draw(img)

for i in range(random.randint(1,10)):
    draw.line(
        [
            (random.randint(1, 250), random.randint(1, 250)),
            (random.randint(1, 250), random.randint(1, 250)),
            (random.randint(1, 250), random.randint(1, 250))
        ],
        fill=(0,0,0)
    )
for i in range(1000):
    draw.point(
        [
            random.randint(1,250),
            random.randint(1,250)
        ],
        fill= (0,0,0)
    )

font_list = list("abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
c_chars = "".join(random.sample(font_list,4))

font = ImageFont.truetype("simsun.ttc", 80)
draw.text((5,5), c_chars,font = font, fill = "green")

params = [1 - float(random.randint(1,2))/100,
          0,
          0,
          0,
          1 - float(random.randint(1,2))/100,
          float(random.randint(1,2))/500,
          0.001,
          float(random.randint(1,1))/500,
          ]
img = img.transform((250,100),Image.PERSPECTIVE,params)
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img.show()