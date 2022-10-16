# API Tribunal de Contas da Uniao - Consulta Consolidada por CNPJ
# Estrategia de versionamento semver.org / major.minor.patch

import requests
import json
from termcolor import colored

def telaInicial():
    print()
    print(colored("     ===================================   ", "red"))
    print(colored("      Inteligência Competitiva Ver 1.0.0   ", "red"))
    print(colored("        -DADOS DA EMPRESA PESQUISADA-      ", "red"))
    print(colored("     ===================================   ", "red"))
    
def telaDadosBasicosCnpj():   
    print()
    print('Razao Social..: {}'.format(arnaDadosTcu["razaoSocial"]))
    print('Nome Fantasia.: {}'.format(arnaDadosTcu["nomeFantasia"]))
    print('CNPJ .........: {}'.format(arnaDadosTcu["cnpj"]))
    print()

def gravaJson():
    with open("resposta.json", "w") as file:
        json.dump(arnaDadosTcu,file,indent=2)

def retornaJson():
    return arnaDadosTcu

telaInicial()
print()

arnaPegaCnpj = str(input('Pesquisar para CNPJ..: '))

arnaEndPoint1 = 'https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/certidoes/{}?seEmitirPDF=false'.format(arnaPegaCnpj)
arnaConTcu = requests.get(arnaEndPoint1)
arnaDadosTcu = arnaConTcu.json()

if (arnaConTcu.status_code != 200):
    print("Falha na Comunicacao com a API...")
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
        
        if ( arnaDadosTcu["certidoes"][arnaIndice]["observacao"] == str("null")):
            print('OBSERVACAO....: N/A')
        else:
            print('OBSERVACAO....: {}'.format(arnaDadosTcu["certidoes"][arnaIndice]["observacao"]))
        arnaIndice += 1
        
print()
print()
print('TOTAL DE BASES PESQUISADAS..: {}'.format(arnaIndice))

