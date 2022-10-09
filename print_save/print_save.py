import sys
from os import listdir, mkdir, path
from tkinter import messagebox

import win32com.client as wsc

import root

# Decide o formato do caminho, por causa do Pyinstaller
if getattr(sys, 'frozen', False):
    application_path = path.dirname(sys.executable)
elif __file__:
    application_path = path.dirname(__file__)
try:
    # Chama Excel
    o = wsc.gencache.EnsureDispatch("Excel.Application")
    o.Visible = True
    # Abre Excel
    excel = 'CÁLCULO_RGE.xls'
    try:
        wb_path = path.join(application_path, excel)
        wb = o.Workbooks.Open(wb_path)
    except:
        messagebox.showerror(
            title="Error Path", message="Necessário colocar o arquivo excel de cálculo (.xls) junto ao arquivo executável (.exe)")
    # Pega o caminho inserido
    poste = root.getInput()
    # Onde vai salvar o print
    user_path = path.expanduser('~')
    new_folder = path.join(user_path, 'CALCULOS')
    if 'CALCULOS' not in listdir(user_path):
        mkdir(new_folder)
    name_poste = f'{poste}.pdf'
    path_pdf = path.join(new_folder, name_poste)
    # Salva o print
    wb.ActiveSheet.ExportAsFixedFormat(0, path_pdf)

except AttributeError as err:
    messagebox.showerror(
        title="Erro no TEMP", message="Erro de compilação do excel.\nApagar 'temp' do seu computador")
