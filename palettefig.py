import math
from PIL import Image, ImageDraw

w, h = 1024, 190

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def createPalette(colors, nome):

    img = Image.new("RGB", (w, h))
    img1 = ImageDraw.Draw(img)
    x0 = 7
    dif = (w - (2 * x0)) / len(colors)
    x1 = x0 + dif
    for i in range(len(colors)):

        cor = rgb_to_hex(colors[i])
        img1.rectangle((x1, 10, x0, h - 10), fill = cor, outline ="#edebeb")
        x0 = x1
        x1 += dif

    arq = nome.split(".")
    file = arq[0] + "-palette.jpg" 
    img.save(file)
