import requests
from bs4 import BeautifulSoup


with open (r'c:\python\html_parser\files\box.html', mode='r', encoding='utf-8') as f:
    res = f.read()

bs = BeautifulSoup(res, 'html.parser')
article_body = bs.select('div.article-body')
fqdn_list = bs.select('ul')


print(fqdn_list) 