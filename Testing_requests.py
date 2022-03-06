 
#SCRAPING
#BeSPecific

import requests
from bs4 import BeautifulSoup

my_url=requests.get('https://www.infodolar.com/cotizacion-dolar-blue.aspx')
soup = BeautifulSoup(my_url.content, 'html.parser')
result = soup.find('#CompraVenta > tbody > tr > td:nth-child(3)')
print(result.text)