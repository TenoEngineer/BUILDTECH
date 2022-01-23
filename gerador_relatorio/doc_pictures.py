# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:35:01 2021

@author: heitor

RELATÓRIO PDF
"""

from docx import Document
from os import path
from docx.enum.text import WD_ALIGN_PARAGRAPH
#import tkinter as tk
from docx2pdf import convert
from pathlib import Path
from docx.shared import Inches
import root as rt
import document as dc
import re

path_fotos = list(rt.getInput())[0]
city = dc.cidade
path_path = Path(path_fotos)
fotos = list(path_path.glob('**\*.jpg'))

fotos = sorted(fotos, key=lambda x: [
               int(k) if k.isdigit() else k for k in re.split('([0-9]+)', x.stem)])

relatorio = str(
    path.abspath(f'{path.dirname(__file__)}\RELATORIO FOTOGRAFICO MODELO A4.docx'))
doc_fotos = Document(relatorio)
dc.doc(doc_fotos)
document = Document(path.abspath(f'{path.dirname(__file__)}\FOTOS.docx'))

for i, image in enumerate(fotos):
    picture = path.join(path_fotos, image)
    p = document.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(picture, width=Inches(10), height=Inches(6))

document.save(path.abspath(f'{path.dirname(__file__)}\FOTOS_TOTAL.docx'))

convert(path.abspath(f'{path.dirname(__file__)}\FOTOS_TOTAL.docx'),
        path.abspath(f'{path_fotos}\{city}_FOTOS.pdf'))


def pic():
    return True
