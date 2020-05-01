"""
GERE UM DICIONÁRIO EM QUE A CHAVE É A TAG H1:

    - o valor deve ser um novo dicionário
    - cada chave do valor deverá ser o valor de atributo
    - cada valor deve ser o texto contido no elemento

    {'h1': {'atr': 'conteudo'}}
"""
from time import sleep
from selenium.webdriver import Chrome

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
bs = Chrome()
bs.get(url)
sleep(3)
val = bs.find_elements_by_tag_name('p')
print(val)
for i in val:
    print(i.text, i.tag_name)
dicio = {
    'h1': {i.get_attribute('atributo'): i.text for i in val}
}


bs.quit()

