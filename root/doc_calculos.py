# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 12:22:13 2021

@author: heitor

RELATÓRIO DE CÁLCULOS

"""

from docx import Document
import os
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx2pdf import convert
from pathlib import Path
from docx.shared import Inches
import root as rt

path_calcu = list(rt.getInput())[0]
city = list(rt.getInput())[2].upper()
path = Path(path_calcu)
calculos = []

for file in os.listdir(path_calcu):
    if '.png' in file:
        calculos.append(file)
doc_calculos = Document(f'{os.path.dirname(__file__)}\MODELO_CALCULOS.docx')
calculos = sorted(calculos, key=lambda x: int(os.path.splitext(x)[0]))

for i, image in enumerate(calculos):
    #picture = os.path.join(path_calcu, image)
    picture = f'{path_calcu}\{image}'
    p = doc_calculos.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(picture, width=Inches(11.3), height=Inches(6.6))
    name_poste = os.path.split(image)
    name = (name_poste[1].split('.'))[0]
    doc_calculos.add_paragraph(
        f'POSTE {name}').paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc_calculos.save(f'{os.path.dirname(__file__)}\CALCULOS_TOTAL.docx')

convert(f'{os.path.dirname(__file__)}\CALCULOS_TOTAL.docx',
        f'{path_calcu}\{city}_CALCULOS.pdf')


def cal():
    return True
