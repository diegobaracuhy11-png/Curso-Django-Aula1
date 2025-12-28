import requests

url = 'https://www.google.com.br' 
response = requests.get(url)

print(response)
print(response.text)

with open ('files/page.html', 'w', encoding= 'UTF-8') as page:
    page.write(response.text)

    #criar uma pasta em files e depois acessando pela pagina do arquivo vc pode acessar o site do codigo 
        