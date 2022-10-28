# Utiliza API Tribunal de Contas da Uniao - Consulta Consolidada por CNPJ
# Utiliza API compras.dados.gov.br // informacoes sicaf
# api.py ver 1.0.0
# Francisco Arnaldo S. Araujo -> netservicero@gmail.com // github.com/fasaraujo

import requests
import json
from termcolor import colored

class Url:
    def __init__(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def conecta(self):
        response = requests.get(self.url)
        return response

def arnaStatusCode(self):
    pass

def telaInicial():
    print()
    print(colored("     ===================================   ", "red"))
    print(colored("      Inteligência Competitiva Ver 1.0.0   ", "red"))
    print(colored("             -Busca de Sanções-            ", "red"))
    print(colored("     ===================================   ", "red"))
    
def telaDadosBasicosCnpj():   
    print()
    print('Razao Social..: {}'.format(arnaDadosTcu["razaoSocial"]))
    print('Nome Fantasia.: {}'.format(arnaDadosTcu["nomeFantasia"]))
    print('CNPJ .........: {}'.format(arnaDadosTcu["cnpj"]))
    print()

def TelaSicafVigente():
    print(colored('-------------------------------------------------------------', "green"))
    print(colored('          IMPEDIMENTOS DE LICITAR VIGENTES NO SICAF          ', 'red', attrs=["reverse", "blink"]))
    print(colored('-------------------------------------------------------------', "green"))      

def TelaSicafHistorico():
    print(colored('-------------------------------------------------------------', "green"))
    print(colored('  HISTORICO DE IMPEDIMENTOS DE LICITAR <NAO VIGENTES> SICAF  ', 'green', attrs=["reverse", "blink"]))
    print(colored('-------------------------------------------------------------', "green"))      

telaInicial()
print()

arnaPegaCnpj = str(input(colored('Pesquisar para CNPJ..: ', 'yellow')))

Tcu = Url('https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/certidoes/{}?seEmitirPDF=false'.format(arnaPegaCnpj))
arnaConTcu = Tcu.conecta()
arnaDadosTcu = arnaConTcu.json()

sicafSancoesVigentes = Url('http://compras.dados.gov.br/fornecedores/v1/ocorrencias_fornecedores.json?cnpj={}&impedido_licitar=true&vigente=sim'.format(arnaPegaCnpj))
sicafSancoesHistorico = Url('http://compras.dados.gov.br/fornecedores/v1/ocorrencias_fornecedores.json?cnpj={}&impedido_licitar=true'.format(arnaPegaCnpj))

if (arnaConTcu.status_code != 200):
    print(colored('Falha na comunicao com a API TCU.', 'red', attrs=["reverse", "blink"]))
else:
    telaDadosBasicosCnpj()
    arnaIndice = 0
    for i in arnaDadosTcu["certidoes"]:
        print(colored("-------------------------------------------------------------", "green"))
        print('EMISSOR......: {}'.format(arnaDadosTcu["certidoes"][arnaIndice]["emissor"]))
        print('TIPO.........: {}'.format(arnaDadosTcu["certidoes"][arnaIndice]["tipo"]))
        print('DATA/HORA....: {}'.format(arnaDadosTcu["certidoes"][arnaIndice]["dataHoraEmissao"]))
        print('DESCRICAO....: {}'.format(arnaDadosTcu["certidoes"][arnaIndice]["descricao"]))
        print('SITUACAO.....: ** {} **'.format(arnaDadosTcu["certidoes"][arnaIndice]["situacao"]))
        
        if not arnaDadosTcu["certidoes"][arnaIndice]["observacao"]:
            print('OBSERVACAO....: N/A')
        else:
            print('OBSERVACAO....: {}'.format(arnaDadosTcu["certidoes"][arnaIndice]["observacao"]))
        arnaIndice += 1
        
print()
print()
print(colored('Comunicando com API SICAF..', 'yellow'))
print()

arnaConSicafVigente = sicafSancoesVigentes.conecta()
arnaDadosJsonSicafVigente = arnaConSicafVigente.json()

if (arnaConSicafVigente.status_code != 200):
    print(colored('Falha na comunicao com a API SICAF.', 'red', attrs=["reverse", "blink"]))
else:
    TelaSicafVigente()
    arnaIndiceSicafVigente = 0
    for percorre in arnaDadosJsonSicafVigente['_embedded']['ocorrenciasFornecedores']:
    
     print('ID...........:',arnaDadosJsonSicafVigente['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafVigente]['id'])
     print('CNPJ.........:',arnaDadosJsonSicafVigente['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafVigente]['cnpj'])
     print('FORNECEDOR...:',arnaDadosJsonSicafVigente['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafVigente]['_links']['fornecedor']['title'])
     print('ID PROCESSO..:',arnaDadosJsonSicafVigente['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafVigente]['numero_processo'])
     print('TIPO ........:',arnaDadosJsonSicafVigente['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafVigente]['_links']['tipo_ocorrencia']['title'])
     print('UASG .........:',arnaDadosJsonSicafVigente['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafVigente]['_links']['uasg']['title'])
     print(colored('-------------------------------------------------------------', "green"))
     arnaIndiceSicafVigente +=1
print()
print()
print(colored('Buscando Historico de impedimentos anteriores <Nao Vigentes>..', 'yellow'))
print()

arnaConSicafHistorico = sicafSancoesHistorico.conecta()
arnaDadosJsonSicafHistorico = arnaConSicafHistorico.json()

if (arnaConSicafHistorico.status_code != 200):
    print(colored('Falha na comunicao com a API SICAF .', 'red', attrs=["reverse", "blink"]))
else:
    TelaSicafHistorico()
    arnaIndiceSicafHistorico = 0
    for percorre2 in arnaDadosJsonSicafHistorico['_embedded']['ocorrenciasFornecedores']:
    
     print('ID...........:',arnaDadosJsonSicafHistorico['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafHistorico]['id'])
     print('CNPJ.........:',arnaDadosJsonSicafHistorico['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafHistorico]['cnpj'])
     print('FORNECEDOR...:',arnaDadosJsonSicafHistorico['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafHistorico]['_links']['fornecedor']['title'])
     print('ID PROCESSO..:',arnaDadosJsonSicafHistorico['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafHistorico]['numero_processo'])
     print('TIPO ........:',arnaDadosJsonSicafHistorico['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafHistorico]['_links']['tipo_ocorrencia']['title'])
     print('UASG .........:',arnaDadosJsonSicafHistorico['_embedded']['ocorrenciasFornecedores'][arnaIndiceSicafHistorico]['_links']['uasg']['title'])
     print(colored('-------------------------------------------------------------', "green"))
     arnaIndiceSicafHistorico +=1

print()
print(colored('Fim de pesquisa..', 'yellow'))
print()

# __name__== '__main__'


