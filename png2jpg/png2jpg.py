from PIL import Image
import os
import tkinter as tk

root = tk.Tk()
root.geometry("550x70")

png_var = tk.StringVar()


def getInput():
    pngs = png_var.get()
    root.quit()
    return pngs


pdf_label = tk.Label(root, text='Caminho PNGs:', font=('calibre', 10, 'bold'))
pdf_entry = tk.Entry(root, textvariable=png_var,
                     font=('calibre', 10, 'normal'), width=60)
pdf_entry.focus_set()
pdf_label.grid(row=0, column=0)
pdf_entry.grid(row=0, column=1)

save_btn = tk.Button(root, text='OK', command=getInput, width=10)
save_btn.grid(row=1, column=1)

root.mainloop()

path = getInput()
pictures = os.listdir(path)
pictures = list(filter(lambda picture: '.png' in picture, pictures))

for pic in pictures:
    print(pic)
    image = Image.open(f'{path}\{pic}')
    name = pic[:-4]
    image.save(f'{path}\{str(name)}.jpg')
    os.remove(f'{path}\{str(pic)}')
