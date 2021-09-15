# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:55:05 2021

@author: heitor
"""

import tkinter as tk
from os import path

root = tk.Tk()
root.iconphoto(False, tk.PhotoImage(file=f'{path.dirname(__file__)}\icon\BuildTech.png'))
root.title('AUTOMAÇÃO RELATÓRIOS')
root.geometry("750x90")

# TODO criar apenas um caminho e fazer o programa reconhecer o que é calculo e foto...

path_var = tk.StringVar()
cidade_var = tk.StringVar()


def getInput():
    path = path_var.get()
    cidade = cidade_var.get()

    return path, cidade


path_label = tk.Label(root, text='Caminho pasta projeto:',
                          font=('calibre', 10, 'bold'))
path_entry = tk.Entry(root, textvariable=path_var,
                          font=('calibre', 10, 'normal'), width=80)

cidade_label = tk.Label(root, text='Nome da cidade:',
                        font=('calibre', 10, 'bold'))
cidade_entry = tk.Entry(root, textvariable=cidade_var,
                        font=('calibre', 10, 'normal'), width=30)

path_label.grid(row=0, column=0, sticky=tk.E)
path_entry.grid(row=0, column=1)
cidade_entry.grid(row=2, column=1, sticky=tk.N+tk.W)
cidade_label.grid(row=2, column=0, sticky=tk.E)

save_btn = tk.Button(root, text='OK', command=getInput, width=15)
save_btn.grid(row=5, column=1)

root.mainloop()
