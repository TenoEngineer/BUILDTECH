# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:02:49 2021

@author: heitor

DESENVOLVIMENTO DO PROGRAMA MAIN
"""

import doc_pictures
import document
import split_pdf
import doc_calculos
import time
from os import path, remove, listdir
from PyPDF2 import PdfFileReader
import sys

if getattr(sys, 'frozen', False):
    application_path = path.dirname(sys.executable)
elif __file__:
    application_path = path.dirname(__file__)
paths = path.dirname(__file__)

fotos_pdf = path.join(doc_pictures.path_fotos,
                      f'{doc_pictures.city}_FOTOS.pdf')
calculos_pdf = path.join(doc_pictures.path_fotos,
                         f'{doc_pictures.city}_CALCULOS.pdf')
fotos_docx = path.join(application_path, 'FOTOS.docx')
fotos_total = path.join(application_path, 'FOTOS_TOTAL.docx')
calculos_total = path.join(application_path, 'CALCULOS_TOTAL.docx')

try:

    def exc():
        split_pdf
        target_size = split_pdf.target_size
        if path.getsize(fotos_pdf) > target_size:
            try:
                remove(fotos_pdf)
            except:
                with open(fotos_pdf) as f:
                    PdfFileReader(f)
                    f.close()
                remove(fotos_pdf)
        if path.getsize(calculos_pdf) > target_size:
            try:
                remove(calculos_pdf)
            except:
                with open(calculos_pdf) as f:
                    PdfFileReader(f)
                    f.close()
                remove(calculos_pdf)

    funcs = [document, doc_pictures, doc_calculos, exc()]

    past = listdir(paths)

    if fotos_docx in past:
        remove(fotos_docx)
    if fotos_total in past:
        remove(fotos_total)
    if calculos_total in past:
        remove(calculos_total)

    funcs

    remove(fotos_docx)
    remove(fotos_total)
    remove(calculos_total)


except:
    remove(fotos_docx)
    remove(fotos_total)
    remove(calculos_total)


if __name__ == '__main__':
    exc()
