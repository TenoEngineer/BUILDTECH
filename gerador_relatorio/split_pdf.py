# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 07:13:49 2021

@author: heitor

SPLIT PDF
"""
import os
from glob import glob
from os import path

from PyPDF2 import PdfFileReader, PdfFileWriter

import root_var as rt

caminho = rt.caminho
city = rt.cidade
calculos = rt.validacao_calculos
fotos = rt.validacao_fotos


def splitPdfs(list):

    if calculos is True or fotos is True:  # Para rodar o split só depois de ter criado os 2 pdfs
        for i in list:

            global target_size_limit
            global target_size

            pdf = PdfFileReader(open(str(i), "rb"))
            size_pdf = path.getsize(str(i))
            target_size_limit = 9
            target_size = target_size_limit*1024*1024
            pages = pdf.getNumPages()

            if size_pdf > target_size:  # SE O ARQUIVO FOR MAIOR DE 9 MB

                list_sizes = []

                for page in range(pages):  # SELECIONA TODAS AS PAGINAS
                    output = PdfFileWriter()
                    output.addPage(pdf.getPage(int(page)))
                    file_name = path.join(
                        caminho, f'{page}.pdf')  # ARQUIVO DE UMA PAGE
                    with open(file_name, 'wb') as out:  # CRIA NOVO ARQUIVO COM UMA PAGINA
                        output.write(out)
                    size_page = path.getsize(
                        file_name)  # TAMANHO DO ARQUIVO
                    list_sizes.append(size_page)  # ADICIONA NA LISTA O TAMANHO

                partition_weight = 0
                list_pages_merge = [[]]

                # PEGA LISTA DO TAMANHO DAS PAGE
                for m, weight in enumerate(list_sizes):
                    if partition_weight + weight < target_size:  # SOMA COM A PRÓXIMA PAGE E VERIFICA SE FICA MAIOR QUE 9MB
                        partition_weight += weight  # FAZ A SOMA DELES
                        # CRIA UMA LISTA DO TOTAL DE PAGINAS QUE FICARÃO EM UM UNICOS PDF
                        list_pages_merge[-1].append(m)
                    else:
                        partition_weight = weight  # SE SOMAR MAIOR QUE 9MB FAZ COM QUE CONTINUE O LOOP
                        # ADICIONA A LISTA EM UMA LISTA
                        list_pages_merge.append([m])

                # LOOP PARA A GERAÇÃO DE PDFS
                for partition, pages in enumerate(list_pages_merge):
                    # NOME DO NOVO PDF: CIDADE_FOTOS_X
                    file_name = f'{str(i)[0:-4]}_{partition}.pdf'
                    output = PdfFileWriter()
                    for page in list_pages_merge[partition]:
                        pdf_marge = PdfFileReader(
                            path.join(caminho, f'{page}.pdf'))
                        output.addPage(pdf_marge.getPage(0))
                    with open(file_name, 'wb') as out:  # CRIA NOVO ARQUIVO COM UMA PAGINA
                        output.write(out)

                for page in range(pdf.getNumPages()):
                    os.remove(path.join(caminho, f'{page}.pdf'))


def target_limit():

    target_size_limit = 9
    target_size = target_size_limit*1024*1024
    return target_size
