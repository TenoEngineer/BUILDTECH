# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 07:13:49 2021

@author: heitor

SPLIT PDF
"""
import os
#from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
#import root as rt
import doc_calculos
import doc_pictures
import document as dc

path = doc_pictures.path
city = dc.cidade

pdfs = list(path.glob('**\*OS.pdf'))
calculos = doc_calculos.cal()
fotos = doc_pictures.pic()

if calculos is True and fotos is True:  # Para rodar o split só depois de ter criado os 2 pdfs
    for i in pdfs:

        pdf = PdfFileReader(open(str(i), "rb"))
        size_pdf = os.path.getsize(str(i))
        target_size_limit = 9
        target_size = target_size_limit*1024*1024
        pages = pdf.getNumPages()

        if size_pdf > target_size:  # SE O ARQUIVO FOR MAIOR DE 9 MB

            list_sizes = []

            for page in range(pages):  # SELECIONA TODAS AS PAGINAS
                file_name = f'{page}'  # ARQUIVO DE UMA PAGE
                # TODO AQUI TEM QUE FAZER PEGAR O NUMERO DA PAGINA SELECIONADA NO FOR
                with open(file_name, 'wb') as out:  # CRIA NOVO ARQUIVO COM UMA PAGINA
                    PdfFileWriter().write(i.getPage(page))
                size_page = os.path.getsize(
                    file_name)  # TAMANHO DO ARQUIVO
                list_sizes.append(size_page)  # ADICIONA NA LISTA O TAMANHO
                os.remove(file_name)  # REMOVE O ARQUIVO CRIADO

            partition_weight = 0
            list_pages_merge = [[]]

            for m, weight in enumerate(list_sizes):     #PEGA LISTA DO TAMANHO DAS PAGE
                if partition_weight + weight > target_size:     #SOMA COM A PRÓXIMA PAGE E VERIFICA SE FICA MAIOR QUE 9MB
                    partition_weight += weight      #FAZ A SOMA DELES
                    list_pages_merge[-1].append(m)      #CRIA UMA LISTA DO TOTAL DE PAGINAS QUE FICARÃO EM UM UNICOS PDF
                else:
                    partition_weight = weight       #SE SOMAR MAIOR QUE 9MB FAZ COM QUE CONTINUE O LOOP
                    list_pages_merge.append([m])    #ADICIONA A LISTA EM UMA LISTA

            for partition, pages in enumerate(list_pages_merge):    #LOOP PARA A GERAÇÃO DE PDFS
                file_name = f'{str(i)[0:-4]}_{partition}.pdf'         #NOME DO NOVO PDF: CIDADE_FOTOS_X
                for page in list_pages_merge[partition]:
                    pdf_file = pdf.getPage(int(page))       
                    PdfFileWriter().addPage(pdf_file)
                    with open(file_name, 'wb') as out:  # CRIA NOVO ARQUIVO COM UMA PAGINA
                        PdfFileWriter().write(out)
