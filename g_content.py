import sqlite3
import os
import json


def get_content(id):
    with open(os.listdir(os.curdir)[id] + '/descr.txt', 'r') as file:
        descr = json.load(file)
        return descr



