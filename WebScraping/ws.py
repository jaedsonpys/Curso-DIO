# pip install bs4
from bs4 import BeautifulSoup
# pip install requests
import requests

url = 'https://google.com'

# recebendo todo o conteúdo da requisição http/https
req = requests.get(url)

html = req.content

# baixando do site o HTML
soup = BeautifulSoup(html, 'html.parser')

# obtendo todos as tags de links da página
print(soup.findAll('a'))

# prettify transforma o conteúdo em string
# print(soup.prettify())