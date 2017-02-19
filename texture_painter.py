# nothing here
''' renders text from csv file
use snippets....
import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
'''
import bpy
import codecs
import csv
from PIL import Image, ImageFont, ImageDraw

def get_backers(csv_filename):
    with codecs.open(csv_filename, 'r', 'utf-8-sig') as stream:
        iterable = csv.reader(stream)
        header = next(iterable)
        for row in iterable:
            backer = dict(zip(header, row))
            yield backer

def render_text_to_file(text_to_render):
    image = Image.new('RGB', (128,128)) # create Image
    draw = ImageDraw.Draw(image) # create image-draw & font object
    fnt = ImageFont.truetype('Daily1915.ttf',50) # draw text to image-draw
    draw.text((0,0), text_to_render, font=fnt, fill=(255,255,255))
    image.save("test2.png")# save image to file


def go():
    print("texture painter starting up")
    # read thcsv
    for backer in get_backers('backers_10.csv'):
        render_text_to_file("wahhoo!")
