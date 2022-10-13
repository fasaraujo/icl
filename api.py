# API Tribunal de Contas da Uniao
# Consulta Consolidada CNPJ

import requests
import json

def gravaJson():
    with open("resposta.json", "w") as file:
        json.dump(arnaDados,file,indent=2)

def retornaJson():
    return arnaDados

#def tela():
#    print("*****************************")
#    print("** Comunicando com a API ..**")
#    print("*****************************")

arnaEndPoint1 = "https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/certidoes/29292707000109?seEmitirPDF=false"
arnaCon = requests.get(arnaEndPoint1)
arnaDados = arnaCon.json()
 
#tela()

if (arnaCon.status_code != 200):
    print("Falha na Comunicacao com a API...")
else:
    print()
    print("     ==============================   ")
    print("      Inteligência Competitiva        ")
    print("     -DADOS DA EMPRESA PESQUISADA-    ")
    print("     ==============================   ")
    print()
    print('Razao Social..: {}'.format(arnaDados["razaoSocial"]))
    print('Nome Fantasia.: {}'.format(arnaDados["nomeFantasia"]))
    print('CNPJ .........: {}'.format(arnaDados["cnpj"]))
    print()

    arnaIndice = 0
    for i in arnaDados["certidoes"]:
        print("-------------------------------------------------------------")
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





