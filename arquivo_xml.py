import os
import xml.etree.ElementTree as Et
from datetime import date

class ReadXml():
    def __init__(self, directory):
        self.directory = directory
    
    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory) 
                if arq.lower().endswith(".xml")]
    
    def nfe_data(self, xml):
        root = Et.parse(xml).getroot()
        nsNFe = {"ns": "https://www.portalfiscal.inf.br/nfe"}

        print("Root:", root)  # Adicionado para verificar o elemento raiz

        ide = root.find("./ns:NFe/ns:infNFe/ns:ide", nsNFe)
        print("Ide:", ide)  # Adicionado para verificar se o elemento ide foi encontrado

        if ide is None:
            return []

        NFe = self.check_none(ide.find("ns:nNf", nsNFe))
        serie = self.check_none(ide.find("ns:serie", nsNFe))
        data_emissao = self.format_date(self.check_none(ide.find("ns:dhEmi", nsNFe)))

        emitente = root.find("./ns:NFe/ns:infNFe/ns:emit", nsNFe)
        print("Emitente:", emitente)  # Adicionado para verificar se o elemento emitente foi encontrado

        if emitente is None:
            return []

        chave = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNFe))
        cnpj_emitente = self.format_cnpj(self.check_none(emitente.find("ns:CNPJ", nsNFe)))
        nome_emitente = self.check_none(emitente.find("ns:xNome", nsNFe))

        valorNfe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", nsNFe))
        data_importacao = date.today().strftime("%d/%m/%Y")
        data_saida = ""
        usuario = ""

        itemNota = 1
        notas = []

        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNFe):
            prod = item.find("ns:prod", nsNFe)
            if prod is None:
                continue

            cod = self.check_none(prod.find("ns:cProd", nsNFe)) 
            qntd = self.check_none(prod.find("ns:qCom", nsNFe))  
            descricao = self.check_none(prod.find("ns:xProd", nsNFe))
            unidade_medida = self.check_none(prod.find("ns:uCom", nsNFe))
            valorProd = self.check_none(prod.find("ns:vProd", nsNFe))

            dados = [NFe, serie, data_emissao, chave, cnpj_emitente, nome_emitente,
                     valorNfe, itemNota,  cod, qntd, descricao, unidade_medida, valorProd,
                     data_importacao, usuario, data_saida]

            notas.append(dados)
            itemNota += 1
        return notas

    def check_none(self, var):
        try:
            return var.text.replace(".", ",") if var is not None else ""
        except AttributeError:
            return ""

    def format_cnpj(self, cnpj):
        try:
            return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
        except TypeError:
            return ""

    def format_date(self, date_str):
        try:
            return f"{date_str[8:10]}/{date_str[5:7]}/{date_str[:4]}"
        except TypeError:
            return ""

if __name__ == "__main__":
    xml_directory = "arquivoqualquer.xml"

    if not os.path.exists(xml_directory):
        print("O arquivo especificado não existe.")
    else:
        xml = ReadXml(xml_directory)
        result = xml.nfe_data(xml_directory)
        print(result)
