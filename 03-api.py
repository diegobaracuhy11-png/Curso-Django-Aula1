import requests
from pprint import pprint
#Pesquisar quantos  nomes que tem em determinado estado
nome = input('Digite um nome para pesquisar:\n')
url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
params = {
    'localidade':25 #PB
}
response = requests.get(url,params=params)
try:
    response.raise_for_status()
except requests.HTTPError as a:
    print (f'erro no  request {a}')
    resultado = None
else:
    resultado=response.json()
    pprint(resultado)
#pprint → serve para mostrar dados grandes de forma organizada, muito útil quando a API retorna listas e dicionários grandes.
