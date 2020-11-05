import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

def convert_uah_to_usd (uah):
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)

    table = soup.find('table', {'class' : 'table-auto'} ) # если find без All то получаем только первое совпадение
    tr = table.find('td', {'class' : 'responsive-hide'})
    tr = tr.text
    tr = tr [:10]
    doll = float(tr)
    summ = uah / doll
    print(summ)

convert_uah_to_usd(float(input()))
