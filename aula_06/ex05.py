"""
OBJETIVO: ENQUANTO FOR PEDIDO, PREENCHER O FORMULÁRIO ESPECÍFICO

- criar entradas de nome e para os formulários
- são 4 formulários, portanto por 4 vezes são pedidos
    - buscar a referência do formulário no span
    - buscar o form cuja classe tenha no seu valor um match com a referência
    - desse form, enviar no input cujo atributo name='nome' a entrada nome
    - desse form, clicar no input cujo atributo type='submit'
    
"""
from time import sleep
from selenium.webdriver import Chrome

url = 'https://selenium.dunossauro.live/exercicio_05.html'

entradas = [
    {'nome': 'Primeiro', 'senha': '1senha'},
    {'nome': 'Segundo', 'senha': '2senha'},
    {'nome': 'Terceiro', 'senha': '3senha'},
    {'nome': 'Quarto', 'senha': '4senha'},
]

browser = Chrome()
browser.get(url)


for vezes in range(4):
    sleep(4)
    referencia = browser.find_element_by_css_selector('span').text
    formulario = browser.find_element_by_css_selector(f"form[class$='{referencia}']")
    
    sleep(2)
    input_nome = formulario.find_element_by_css_selector("input[name='nome']")
    input_senha = formulario.find_element_by_css_selector('input[name="senha"]')
    
    input_nome.send_keys(entradas[vezes]['nome'])
    input_senha.send_keys(entradas[vezes]['senha'])

    sleep(1)
    formulario.find_element_by_css_selector('input[type="submit"]').click()
