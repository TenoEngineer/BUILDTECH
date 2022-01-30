# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 06:44:36 2021

@author: heitor

PDF TO PNG
"""
import os
from numpy import tile
from pdf2image import convert_from_path
import root
from tkinter import messagebox

path = root.getInput()

try:
    pictures = os.listdir(path)
    pictures = list(filter(lambda picture: '.pdf' in picture, pictures))
except:
    messagebox.showerror(
        title='ERROR', message='Favor rever o caminho inserido.')

poppler = 'poppler-0.68.0/bin'
user_path = os.path.expanduser('~')
poppler_path = os.path.join(user_path, poppler)

for pic in pictures:
    image = convert_from_path(os.path.join(
        path, pic), poppler_path=poppler_path)
    images = list(range(len(image)))
    name_pdf = pic.replace('POSTE', '')
    name_pdf = name_pdf.replace(' ', '')
    name_png = name_pdf.replace('.pdf', '.png')
    image = image[0]
    image.save(os.path.join(path, name_png), 'PNG')
    os.remove(os.path.join(path, pic))
    print(f'Gerado arquivo: {name_png}')
