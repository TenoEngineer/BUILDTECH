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
from os import path, remove

document
doc_pictures
doc_calculos
split_pdf

path = path.dirname(__file__)
remove(f'{path}\FOTOS.docx')
remove(f'{path}\FOTOS_TOTAL.docx')
remove(f'{path}\CALCULOS_TOTAL.docx')
