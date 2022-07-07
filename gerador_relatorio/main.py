# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:02:49 2021

@author: heitor

DESENVOLVIMENTO DO PROGRAMA MAIN
"""

import sys
from glob import glob
from os import listdir, path, remove
from pathlib import Path

from PyPDF2 import PdfFileReader

import reports
import root_var as rt

caminho = rt.caminho
cidade = rt.cidade
validacao_fotos = rt.validacao_fotos
validacao_calculos = rt.validacao_calculos

if getattr(sys, 'frozen', False):
    application_path = path.dirname(sys.executable)
elif __file__:
    application_path = path.dirname(__file__)

fotos_pdf = path.join(caminho, f'{cidade}_FOTOS.pdf')
calculos_pdf = path.join(caminho, f'{cidade}_CALCULOS.pdf')
fotos_docx = path.join(application_path, 'FOTOS.docx')
fotos_total = path.join(application_path, 'FOTOS_TOTAL.docx')
calculos_total = path.join(application_path, 'CALCULOS_TOTAL.docx')

try:
    reports.main()
    try:
        remove(fotos_docx)
    except:
        pass
    try:
        remove(fotos_total)
    except:
        pass
    try:
        remove(calculos_total)
    except:
        pass

except:
    try:
        remove(fotos_docx)
    except:
        pass
    try:
        remove(fotos_total)
    except:
        pass
    try:
        remove(calculos_total)
    except:
        pass

try:
    path_path = Path(caminho)
    scr = list(path_path.glob('*.scr'))
    csv = list(path_path.glob('*.csv'))
    bak = list(path_path.glob('*.bak'))
    for i in scr:
        remove(i)
    for i in csv:
        remove(i)
    for i in bak:
        remove(i)
except:
    pass
