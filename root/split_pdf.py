# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 07:13:49 2021

@author: heitor

SPLIT PDF
"""
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import root as rt
import doc_calculos
import doc_pictures

foto_path = list(rt.getInput())[1]
calcu_path = list(rt.getInput())[0]
city = list(rt.getInput())[2].upper()

pdfs = [f'{foto_path}\{city}_FOTOS.pdf', f'{calcu_path}\{city}_CALCULOS.pdf']
calculos = doc_calculos.cal()
fotos = doc_pictures.pic()

if calculos is True and fotos is True:  # Para rodar o split só depois de ter criado os 2 pdfs
    for i in pdfs:

        pdf = PdfFileReader(open(i, "rb"))
        size_pdf = os.path.getsize(i)
        target_size_limit = 9
        target_size = target_size_limit*1024*1024
        pages = pdf.numPages

        if size_pdf > target_size:  # SE O ARQUIVO FOR MAIOR DE 9 MB

            list_sizes = []

            for page in range(pages):  # SELECIONA TODAS AS PAGINAS
                file_name = f'{page}'  # ARUIVO DE UMA PAGE
                with open(file_name, 'wb') as out:  # CRIA NOVO ARQUIVO COM UMA PAGINA
                    PdfFileWriter().write(out)
                size_page = os.path.getsize(
                    file_name)  # TAMANHO DO ARQUIVO
                list_sizes.append(size_page)  # ADICIONA NA LISTA O TAMANHO
                os.remove(file_name)  # REMOVE O ARQUIVO CRIADO

            partition_weight = 0
            list_pages_merge = [[]]

            for m, weight in enumerate(list_sizes):
                if partition_weight + weight > target_size:
                    partition_weight += weight
                    list_pages_merge[-1].append(m)
                else:
                    partition_weight = weight
                    list_pages_merge.append([m])

            for partition, pages in enumerate(list_pages_merge):
                file_name = f'{i[:-4]}_{partition}.pdf'
                for page in list_pages_merge[partition]:
                    pdf_file = pdf.getPage(int(page))
                    PdfFileWriter().addPage(pdf_file)
                    with open(file_name, 'wb') as out:  # CRIA NOVO ARQUIVO COM UMA PAGINA
                        PdfFileWriter().write(out)
