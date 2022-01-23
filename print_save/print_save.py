#from ast import Index
import win32com.client as wsc
from os import path, mkdir, listdir, remove
from tkinter import messagebox
import root

# CASO OCORRA ALGUM ERRO DE 00020813-0000-0000-C000-000000000046x0x1x9
# APAGAR O TEMP DO PC E RODAR NOVAMENTE

try:
# PRINT DA TELA DO EXCEL
    o = wsc.gencache.EnsureDispatch("Excel.Application")
    o.Visible = True

    wb_path = f'{path.dirname(__file__)}\CÁLCULO_RGE.xls'
    wb = o.Workbooks.Open(wb_path)

    poste = root.getInput()

    user_path = path.expanduser('~')
    new_folder = path.join(user_path, 'CALCULOS')
    if 'CALCULOS' not in listdir(user_path):
        mkdir(new_folder)
    path_pdf = f'{new_folder}\{poste}.pdf'  # COLOCA O INPUT
    print_area = '$A$1:$AI$54'

    #ws = wb.Worksheets(index)
    ws = wb.Worksheets[1]

    ws.PageSetup.Zoom = False

    ws.PageSetup.FitToPagesTall = 1

    ws.PageSetup.FitToPagesWide = 1

    ws.PageSetup.PrintArea = print_area

    ws.Select()
    wb.Activate
    wb.ExportAsFixedFormat(0, path_pdf)

except AttributeError as err:
    messagebox.showerror(title="Erro no TEMP", message="Erro de compilação do excel.\nApagar 'temp' do seu computador")