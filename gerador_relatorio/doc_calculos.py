# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 12:22:13 2021

@author: heitor

RELATÓRIO DE CÁLCULOS

"""

from docx import Document
import document as dc
from os import path
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx2pdf import convert
from pathlib import Path
from docx.shared import Inches
import re
import doc_pictures
import sys

path_calcu = doc_pictures.path_fotos
city = dc.cidade
path_path = Path(path_calcu)
calculos = list(path_path.glob('**\*.png'))
calculos = sorted(calculos, key=lambda x: [int(
    k) if k.isdigit() else k for k in re.split('([0-9]+)', x.stem)])
modelo_calculos = 'MODELO_CALCULOS.docx'
calculos_total = 'CALCULOS_TOTAL.docx'

if getattr(sys, 'frozen', False):
    application_path = path.dirname(sys.executable)
elif __file__:
    application_path = path.dirname(__file__)

doc_calculos = Document(path.join(application_path, modelo_calculos))

for i, image in enumerate(calculos):
    picture = str(image)
    p = doc_calculos.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(picture, width=Inches(11.3), height=Inches(6.6))
    name_poste = path.split(image)
    name = (name_poste[1].split('.'))[0]
    doc_calculos.add_paragraph(
        f'POSTE {name}').paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc_calculos.save(path.join(application_path, calculos_total))

convert(path.join(application_path, calculos_total),
        path.join(path_calcu, f'{city}_CALCULOS.pdf'))


def cal():
    return True


if __name__ == '__main__':
    cal()
