import os
import tkinter

from PIL import Image

import root


def convert():

    app = root.Janela()
    tkinter.mainloop()
    path = app.getInput()
    pictures = os.listdir(path)
    pictures = list(filter(lambda picture: '.jpg' in picture, pictures))

    for pic in pictures:
        print(pic)
        image = Image.open(os.path.join(path, pic))
        name = pic[:-4]
        new_name = os.path.join(path, str(name))
        image.save(f'{new_name}.png')
        os.remove(os.path.join(path, str(pic)))
