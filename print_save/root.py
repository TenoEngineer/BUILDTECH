import tkinter as tk

root = tk.Tk()
root.geometry("130x50")

poste_var = tk.StringVar()


def getInput():
    root.quit()
    poste = poste_var.get()
    return poste.upper()


poste_label = tk.Label(root, text='Poste:', font=('calibre', 10, 'bold'))
poste_entry = tk.Entry(root, textvariable=poste_var,
                       font=('calibre', 10, 'normal'), width=10)
poste_entry.focus_set()

poste_label.grid(row=0, column=0)
poste_entry.grid(row=0, column=1)

save_btn = tk.Button(root, text='OK', command=getInput, width=8)
save_btn.grid(row=1, column=1)

root.mainloop()

if __name__ == '__main__':
    getInput()
