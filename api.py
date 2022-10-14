# API Tribunal de Contas da Uniao - Consulta Consolidada por CNPJ
# Estrategia de versionamento semver.org / major.minor.patch

import requests
import json
from termcolor import colored

def gravaJson():
    with open("resposta.json", "w") as file:
        json.dump(arnaDados,file,indent=2)

def retornaJson():
    return arnaDados

#def tela():
#    print("*****************************")
#    print("** Comunicando com a API ..**")
#    print("*****************************")

arnaEndPoint1 = "https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/certidoes/76535764000143?seEmitirPDF=false"
arnaCon = requests.get(arnaEndPoint1)
arnaDados = arnaCon.json()
 
#tela()

if (arnaCon.status_code != 200):
    print("Falha na Comunicacao com a API...")
else:
    print()
    print(colored("     ===================================   ", "red"))
    print(colored("      Inteligência Competitiva Ver 1.0.0   ", "red"))
    print(colored("        -DADOS DA EMPRESA PESQUISADA-      ", "red"))
    print(colored("     ===================================   ", "red"))
    print()
    print('Razao Social..: {}'.format(arnaDados["razaoSocial"]))
    print('Nome Fantasia.: {}'.format(arnaDados["nomeFantasia"]))
    print('CNPJ .........: {}'.format(arnaDados["cnpj"]))
    print()

    arnaIndice = 0
    for i in arnaDados["certidoes"]:
        print(colored("-------------------------------------------------------------", "green"))
        print('EMISSOR......: {}'.format(arnaDados["certidoes"][arnaIndice]["emissor"]))
        print('TIPO.........: {}'.format(arnaDados["certidoes"][arnaIndice]["tipo"]))
        print('DATA/HORA....: {}'.format(arnaDados["certidoes"][arnaIndice]["dataHoraEmissao"]))
        print('DESCRICAO....: {}'.format(arnaDados["certidoes"][arnaIndice]["descricao"]))
        print('SITUACAO.....: ** {} **'.format(arnaDados["certidoes"][arnaIndice]["situacao"]))
        
        if ( arnaDados["certidoes"][arnaIndice]["observacao"] == str("null")):
            print('OBSERVACAO....: N/A')
        else:
            print('OBSERVACAO....: {}'.format(arnaDados["certidoes"][arnaIndice]["observacao"]))
        arnaIndice += 1
        
print()
print()
print('TOTAL DE BASES PESQUISADAS..: {}'.format(arnaIndice))

# teste
#y = retornaJson()
#print(y)





