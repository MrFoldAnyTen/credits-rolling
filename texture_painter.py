# nothing here
''' renders text from csv file
use snippets....
import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
'''
import codecs
import csv

def get_backers(csv_filename):
    with codecs.open(csv_filename, 'r', 'utf-8-sig') as stream:
        iterable = csv.reader(stream)
        header = next(iterable)
        for row in iterable:
            backer = dict(zip(header, row))
            yield backer

def go():
    print("texture painter starting up")
    # read thcsv
    for backer in get_backers('backers_10.csv'):
        print(backer)
