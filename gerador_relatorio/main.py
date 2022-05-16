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

import doc_calculos
import doc_pictures
import root_var as rt
import split_pdf

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
    target_size = split_pdf.target_limit()
    pic = doc_pictures.fotos()
    cal = doc_calculos.calculos()
    if pic is True and cal is False:
        pdfs = glob(path.join(caminho, "*.pdf"))
        split_pdf.splitPdfs(pdfs)
        if path.getsize(fotos_pdf) > target_size:
            remove(fotos_pdf)
    elif cal is True and pic is False:
        pdfs = glob(path.join(caminho, "*.pdf"))
        split_pdf.splitPdfs(pdfs)
        if path.getsize(calculos_pdf) > target_size:
            remove(calculos_pdf)
    elif pic is True and cal is True:
        pdfs = glob(path.join(caminho, "*.pdf"))
        split_pdf.splitPdfs(pdfs)
        if int(path.getsize(fotos_pdf)) > int(target_size):
            remove(fotos_pdf)
        if int(path.getsize(calculos_pdf)) > int(target_size):
            remove(calculos_pdf)
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
