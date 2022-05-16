from tkinter import messagebox

import jpg2png as j

try:
    j.convert()
except:
    messagebox.showerror(
        title="Erro", message="Ocorreu um erro, favor refazer o processo")
