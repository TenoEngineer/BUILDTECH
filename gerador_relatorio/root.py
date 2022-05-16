# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:55:05 2021

@author: heitor
"""

import tkinter as tk


class Janela(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('AUTOMAÇÃO RELATÓRIOS')
        self.geometry("550x100")

        self.path_var = tk.StringVar(self)
        self.cidade_var = tk.StringVar(self)
        self.chkFotos = tk.BooleanVar(self)
        self.chkCalculos = tk.BooleanVar(self)

        self.path_label = tk.Label(self, text='Caminho pasta projeto:', font=(
            'calibre', 10, 'bold')).grid(row=0, column=0)
        self.path_entry = tk.Entry(self, textvariable=self.path_var,
                                   font=('calibre', 10, 'normal'), width=45)
        self.path_entry.focus_set()
        self.cidade_label = tk.Label(self, text='Nome da cidade:', font=(
            'calibre', 10, 'bold')).grid(row=2, column=0)
        self.cidade_entry = tk.Entry(self, textvariable=self.cidade_var,
                                     font=('calibre', 10, 'normal'), width=45)

        self.path_entry.grid(row=0, column=1)
        self.cidade_entry.grid(row=2, column=1)

        tk.Button(self, text='OK', command=self.getInput,
                  width=15).grid(row=4, column=1)

        tk.Button(self, text="Exit",
                  command=self.destroy, width=10).grid(row=4, column=0)

        self.chkFotos.set(True)
        self.chkCalculos.set(True)

        self.chkBoxFotos = tk.Checkbutton(
            self, text='Fotos', var=self.chkFotos)
        self.chkBoxFotos.grid(row=3, column=0)
        self.chkBoxCal = tk.Checkbutton(
            self, text='Calculos', var=self.chkCalculos)
        self.chkBoxCal.grid(row=3, column=1)

    def getInput(self) -> str:
        path = self.path_var.get()
        cidade = self.cidade_var.get()
        fotos = self.chkFotos.get()
        calculos = self.chkCalculos.get()
        self.quit()
        return path, cidade, fotos, calculos


if __name__ == '__main__':
    app = Janela()
    app.mainloop()
