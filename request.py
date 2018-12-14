import cv2
import numpy as np 
import sqlite3
import os
import requests, shutil
conn = sqlite3.connect('database.db')
c = conn.cursor()

f = open('out.txt', 'r')
name = f.read() 
c.execute("select * from users where post = (?);", (name,))
result = c.fetchall()

with open('info.txt', 'w') as f2:
        print(result, file=f2)
     


#тут нужно скачать файл с сервака на коп
