# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:34:23 2021

@author: heitor

INSERE O NOME DA CIDADE NO DOCX
"""

import root as rt
from os import path
import sys

cidade = list(rt.getInput())[1].upper()
fotos = 'FOTOS.docx'


def doc(document):
    for section in document.sections:
        header = section.header
        header.paragraphs[1].text = 'LOCALIDADE: CIDADE - RS'
        header.paragraphs[1].text = header.paragraphs[1].text.replace(
            "CIDADE", cidade)
        header.paragraphs[1].bold = True

    if getattr(sys, 'frozen', False):
        application_path = path.dirname(sys.executable)
    elif __file__:
        application_path = path.dirname(__file__)

    document.save(path.join(application_path, fotos))


if __name__ == '__main__':
    doc()
