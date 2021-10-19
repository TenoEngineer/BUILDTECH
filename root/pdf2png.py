# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 06:44:36 2021

@author: heitor

PDF TO PNG
"""
import os
from pdf2image import convert_from_path
import tkinter as tk

root = tk.Tk()
root.geometry("550x70")

pdf_var = tk.StringVar()


def getInput():
    pdfs = pdf_var.get()
    return pdfs


pdf_label = tk.Label(root, text='Caminho pdfs:', font=('calibre', 10, 'bold'))
pdf_entry = tk.Entry(root, textvariable=pdf_var,
                     font=('calibre', 10, 'normal'), width=60)

pdf_label.grid(row=0, column=0)
pdf_entry.grid(row=0, column=1)

save_btn = tk.Button(root, text='OK', command=getInput, width=10)
save_btn.grid(row=1, column=1)

root.mainloop()

path = getInput()
pictures = os.listdir(path)
pictures = list(filter(lambda picture: '.pdf' in picture, pictures))

user_path = os.path.expanduser('~')
poppler_path = os.path.join(user_path, 'poppler-0.68.0/bin')

for pic in pictures:
    # print(pic[6:-4])
    print(pic)
    image = convert_from_path(os.path.join(
        path, pic), poppler_path=poppler_path)
    images = list(range(len(image)))
    # for i in range(len(image)):
    pic = pic.replace('POSTE', '')
    pic = pic.replace(' ', '')
    pic = pic.replace('.pdf', '')
    name = pic
    image = image[0]
    image.save(f'{path}\{str(name)}.png', 'PNG')
