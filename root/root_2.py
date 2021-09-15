# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:55:05 2021

@author: heitor
"""

import tkinter as tk

root = tk.Tk()
root.geometry("300x90")

# TODO criar apenas um caminho e fazer o programa reconhecer o que é calculo e foto...

calculos_var = tk.StringVar()
fotos_var = tk.StringVar()
cidade_var = tk.StringVar()


def getInput():
    calculos = calculos_var.get()
    fotos = fotos_var.get()
    cidade = cidade_var.get()

    return calculos, fotos, cidade


calculos_label = tk.Label(root, text='Caminho calculos:',
                          font=('calibre', 10, 'bold'))
calculos_entry = tk.Entry(root, textvariable=calculos_var,
                          font=('calibre', 10, 'normal'))

fotos_label = tk.Label(root, text='Caminho fotos:',
                       font=('calibre', 10, 'bold'))
fotos_entry = tk.Entry(root, textvariable=fotos_var,
                       font=('calibre', 10, 'normal'))

cidade_label = tk.Label(root, text='Nome da cidade:',
                        font=('calibre', 10, 'bold'))
cidade_entry = tk.Entry(root, textvariable=cidade_var,
                        font=('calibre', 10, 'normal'))

calculos_label.grid(row=0, column=0)
calculos_entry.grid(row=0, column=1)
fotos_label.grid(row=1, column=0)
fotos_entry.grid(row=1, column=1)
cidade_entry.grid(row=2, column=1)
cidade_label.grid(row=2, column=0)

save_btn = tk.Button(root, text='OK', command=getInput, width=10)
save_btn.grid(row=5, column=1)

root.mainloop()
