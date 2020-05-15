"""
OBJETIVO: PREENCHER 5 VEZES UM FORMULÁRIO ALEATÓRIO

    - 5 vezes
        - obter do segundo <p> do <header> a referência do formulário a se preenchido
        - procurar um <form> em que class=referência
        - através de <form> obter os <input> em que name="nome" e name="senha"

        - enviar entradas para esses dois <input>
        - obter de <form> o <input> tal que type="submit" e clicar neste elemento

"""

from selenium.webdriver import Chrome
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_06.html'

entradas = [
    {'nome': 'Primeiro', 'senha': '1senha'},
    {'nome': 'Segundo', 'senha': '2senha'},
    {'nome': 'Terceiro', 'senha': '3senha'},
    {'nome': 'Quarto', 'senha': '4senha'},
    {'nome': 'Quinto', 'senha': '5senha'}
]

browser = Chrome()
browser.get(url)

for vezes in range(5):
    sleep(4)
    referencia = browser.find_element_by_css_selector('header p:nth-child(2)').text.split()[-1]
    form = browser.find_element_by_css_selector(f'form[class$="{referencia}"]')
    
    sleep(2)
    input_nome = form.find_element_by_css_selector('input[name="nome"]')
    input_senha = form.find_element_by_css_selector('input[name="senha"]')

    input_nome.send_keys(entradas[vezes]["nome"])
    input_senha.send_keys(entradas[vezes]["senha"])

    form.find_element_by_css_selector('input[type="submit"]').click()

