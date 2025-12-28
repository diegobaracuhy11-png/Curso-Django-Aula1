import requests

url = 'https://www.httpbin.org/post'
data = {
    'pessoa':{
        'nome': 'Diego',
        'Profissao': 'polidor'
    }
}
paramentro = {
    'dataIni':'2025.01.01',
    'datafim':'2025.12.30'
}

response = requests.post (url, json=data)
print(response)
print(response.text)

#gerando request e analisando resposta
 