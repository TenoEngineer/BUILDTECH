from ast import Index
import win32com.client as wsc
import tkinter as tk

# JANELA PAARA INSERIR O NÚMERO DO POSTE
root = tk.Tk()
root.geometry("130x50")

poste_var = tk.StringVar()


def getInput():
    poste = poste_var.get()
    return poste


poste_label = tk.Label(root, text='Poste:', font=('calibre', 10, 'bold'))
poste_entry = tk.Entry(root, textvariable=poste_var,
                       font=('calibre', 10, 'normal'), width=10)

poste_label.grid(row=0, column=0)
poste_entry.grid(row=0, column=1)

save_btn = tk.Button(root, text='OK', command=getInput, width=8)
save_btn.grid(row=1, column=1)


# PRINT DA TELA DO EXCEL
o = wsc.gencache.EnsureDispatch("Excel.Application")
o.Visible = True

wb_path = r"C:\Users\heito\OneDrive\Informações Projetos\PLANILHA CÁLCULO RGE - CEEE 2.xls"
wb = o.Workbooks.Open(wb_path)

root.mainloop()

poste = getInput()

path_pdf = (
    r'C:\Users\heito\OneDrive\Executando\BUILDTECH\{poste}').format(poste=poste)  # COLOCA O INPUT
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