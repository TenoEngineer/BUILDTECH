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
from os import path, remove, listdir
import time


def exc():
    split_pdf
    target_size = split_pdf.target_size
    time.sleep(5)
    if path.getsize(f'{doc_pictures.path_fotos}\{doc_pictures.city}_FOTOS.pdf') > target_size:
        time.sleep(3)
        remove(f'{doc_pictures.path_fotos}\{doc_pictures.city}_FOTOS.pdf')
    if path.getsize(f'{doc_pictures.path_fotos}\{doc_pictures.city}_CALCULOS.pdf') > target_size:
        time.sleep(3)
        remove(f'{doc_pictures.path_fotos}\{doc_pictures.city}_CALCULOS.pdf')


funcs = [document, doc_pictures, doc_calculos, exc()]

paths = path.dirname(__file__)

past = listdir(paths)
if f'{paths}\FOTOS.docx' in past:
    remove(f'{paths}\FOTOS.docx')
if f'{paths}\FOTOS_TOTAL.docx' in past:
    remove(f'{paths}\FOTOS_TOTAL.docx')
if f'{paths}\CALCULOS_TOTAL.docx' in past:
    remove(f'{paths}\CALCULOS_TOTAL.docx')


try:
    funcs

    remove(f'{paths}\FOTOS.docx')
    remove(f'{paths}\FOTOS_TOTAL.docx')
    remove(f'{paths}\CALCULOS_TOTAL.docx')
except:
    remove(f'{paths}\FOTOS.docx')
    remove(f'{paths}\FOTOS_TOTAL.docx')
    remove(f'{paths}\CALCULOS_TOTAL.docx')
