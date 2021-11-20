from copy import deepcopy

from PIL import Image, ImageDraw
import random
from random import randrange

size = 400


def rectangle(amount, color):
    for i in range(amount):  # prostokąt
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x1 = randrange(5, 360)
        y1 = randrange(5, 360)
        x2 = randrange(x1 + 5, 395)
        y2 = randrange(y1 + 5, 395)
        draw.rectangle((x1, y1, x2, y2), fill=(r, g, b), outline=(r, g, b))
        no = i
        file = 'rectangle/' + 'rectangle' + str(no) + '.png'
        img.save(file)


def ellipse(amount, color):
    for i in range(amount):  # elipsa
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x1 = randrange(5, 360)
        y1 = randrange(5, 360)
        x2 = randrange(x1 + 5, 395)
        y2 = randrange(y1 + 5, 395)
        draw.ellipse((x1, y1, x2, y2), fill=(r, g, b), outline=(r, g, b))
        no = i
        file = 'ellipse/' + 'ellipse' + str(no) + '.png'
        img.save(file)


def square(amount, color):
    for i in range(amount):  # kwadrat
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x1 = randrange(5, 360)
        y1 = randrange(5, 360)
        width = randrange(5, min(395 - x1, 395 - y1))
        x2 = x1 + width
        y2 = y1 + width
        draw.rectangle((x1, y1, x2, y2), fill=(r, g, b), outline=(r, g, b))
        no = i
        file = 'square/' + 'square' + str(no) + '.png'
        img.save(file)


def circle(amount, color):
    for i in range(amount):  # kolo
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        x1 = randrange(5, 360)
        y1 = randrange(5, 360)
        width = randrange(5, min(395 - x1, 395 - y1))
        x2 = x1 + width
        y2 = y1 + width
        draw.ellipse((x1, y1, x2, y2), fill=(r, g, b), outline=(r, g, b))
        no = i
        file = 'circle/' + 'circle' + str(no) + '.png'
        img.save(file)


def trianle(amount, color):
    for i in range(amount):  # kolo
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        x1 = randrange(5, 395)
        y1 = randrange(5, 395)
        x2 = randrange(5, 395)
        y2 = randrange(5, 395)
        x3 = randrange(5, 395)
        y3 = randrange(5, 395)
        draw.polygon((x1, y1, x2, y2, x3, y3), fill=(r, g, b), outline=(r, g, b))

        no = i
        file = 'triangle/' + 'triangle' + str(no) + '.png'
        img.save(file)


def deltoid(amount, color):
    for i in range(amount):  # kolo
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        center_x = randrange(30, 370)
        center_y = randrange(30, 370)

        width = 1000
        while (center_x + width) > 395 or (center_x - width) < 5:
            width = randrange(20, 100)

        h1 = 1000
        while (center_y + h1) > 395 or (center_y - h1) < 5:
            h1 = randrange(20, 200)

        h2 = 1000
        while (center_y + h2) > 395 or (center_y - h2) < 5:
            h2 = randrange(20, 200)

        x1 = center_x - width
        x2 = center_x + width
        x3 = deepcopy(center_x)
        x4 = deepcopy(center_x)
        y1 = deepcopy(center_y)
        y2 = deepcopy(center_y)
        y3 = center_y + h1
        y4 = center_y - h2

        draw.polygon((x1, y1, x2, y2, x3, y3), fill=(r, g, b), outline=(r, g, b))
        draw.polygon((x1, y1, x2, y2, x4, y4), fill=(r, g, b), outline=(r, g, b))

        no = i
        file = 'deltoid/' + 'deltoid' + str(no) + '.png'
        img.save(file)


def rhombus(amount, color):
    for i in range(amount):  # kolo
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        center_x = randrange(30, 370)
        center_y = randrange(30, 370)

        width = 1000
        while (center_x + width) > 395 or (center_x - width) < 5:
            width = randrange(20, 100)

        height = 1000
        while (center_y + height) > 395 or (center_y - height) < 5:
            height = randrange(20, 200)

        x1 = center_x - width
        x2 = center_x + width
        x3 = deepcopy(center_x)
        x4 = deepcopy(center_x)
        y1 = deepcopy(center_y)
        y2 = deepcopy(center_y)
        y3 = center_y + height
        y4 = center_y - height

        draw.polygon((x1, y1, x2, y2, x3, y3), fill=(r, g, b), outline=(r, g, b))
        draw.polygon((x1, y1, x2, y2, x4, y4), fill=(r, g, b), outline=(r, g, b))

        no = i
        file = 'rhombus/' + 'rhombus' + str(no) + '.png'
        img.save(file)


def parallelogram(amount, color):
    for i in range(amount):  # kolo
        if color:
            r = randrange(0, 255)
            g = randrange(0, 255)
            b = randrange(0, 255)
        else:
            r, g, b = 255

        img = Image.new('RGB', (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        x1 = randrange(30, 360)
        y1 = randrange(30, 360)
        x2 = randrange(x1 + 10, 380)
        y2 = randrange(y1 + 10, 380)

        extra_width = 1000
        while (x2 + extra_width) > 395 or (x1 - extra_width) < 5:
            extra_width = randrange(10, 100)

        x3 = x1 - extra_width
        x4 = x2 + extra_width

        draw.rectangle((x1, y1, x2, y2), fill=(r, g, b), outline=(r, g, b))
        draw.polygon((x1, y1, x1, y2, x3, y2), fill=(r, g, b), outline=(r, g, b))
        draw.polygon((x2, y1, x2, y2, x4, y1), fill=(r, g, b), outline=(r, g, b))

        no = i
        file = 'parallelogram/' + 'parallelogram' + str(no) + '.png'
        img.save(file)


color = True
# rectangle(1000, color)
# square(1000, color)
# ellipse(1000, color)
# circle(1000, color)
trianle(1000, color)
deltoid(1000, color)
rhombus(1000, color)
parallelogram(1000, color)
