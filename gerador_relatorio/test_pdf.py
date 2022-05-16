from fpdf import FPDF

#nome_cidade = "eai brow"
#num_poste = 200
#caminho_poste = r'C:\Users\heito\OneDrive\Executando\BUILDTECH\26-02-2022 - CAXIAS DO SUL - BITCOM - AREA 31B - LOTE 46\RELATÓRIO DE FOTOS BITCOM CAXIAS - ÁREA 31B - LOTE 46\POSTE (2).jpg'


class PDF(FPDF):
    def header(self, nome_cidade) -> None:
        self.set_font("Arial", "B", 11)
        self.cell(-20)
        # Framed title
        self.cell(
            320, 10, 'RELATÓRIO FOTOGRÁFICO', 0, 0, 'C')
        self.cell(
            -320, 20, 'PROJETO DE COMPARTILHAMENTO DE INFRAESTRUTURA', 0, 0, 'C')
        self.cell(
            320, 30, f'LOCALIDADE: {nome_cidade} - RS', 0, 0, 'C')


class relatorio_fotos():
    def gerar_pdf(self, num_poste, caminho_poste):
        self = PDF()
        self = PDF(orientation="L")
        self.add_page()
        self.image(caminho_poste, x=10, y=30, w=275, h=160)
        self.text(140, 200, txt=f'Poste {num_poste}')
        self.output("test.pdf", "F")


PDF.header(nome_cidade='CAXIAS DO SUL')
relatorio_fotos.gerar_pdf(
    102, r'C:\Users\heito\OneDrive\Executando\BUILDTECH\26-02-2022 - CAXIAS DO SUL - BITCOM - AREA 31B - LOTE 46\RELATÓRIO DE FOTOS BITCOM CAXIAS - ÁREA 31B - LOTE 46\POSTE (2).jpg')
