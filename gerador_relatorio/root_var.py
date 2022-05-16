import tkinter

import root

app = root.Janela()
tkinter.mainloop()
caminho = app.getInput()[0]
cidade = app.getInput()[1].upper()
validacao_fotos = app.getInput()[2]
validacao_calculos = app.getInput()[3]
