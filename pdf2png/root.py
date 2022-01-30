import tkinter as tk

root = tk.Tk()
root.geometry("550x70")

pdf_var = tk.StringVar()


def getInput():
    pdfs = pdf_var.get()
    root.quit()
    return pdfs


pdf_label = tk.Label(root, text='Caminho pdfs:', font=('calibre', 10, 'bold'))
pdf_entry = tk.Entry(root, textvariable=pdf_var,
                     font=('calibre', 10, 'normal'), width=60)
pdf_entry.focus_set()

pdf_label.grid(row=0, column=0)
pdf_entry.grid(row=0, column=1)

save_btn = tk.Button(root, text='OK', command=getInput, width=8)
save_btn.grid(row=1, column=1)

root.mainloop()
