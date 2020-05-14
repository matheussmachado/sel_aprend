from selenium.webdriver import Chrome
from time import sleep
from pprint import pprint

"""
1 - Obter um dicionário com o nome das aulas contendo o link para elas
    {'nomeAula': 'link'}

2 - Navegar até o exercicio 3
"""

url = 'http://selenium.dunossauro.live/aula_04.html'
brwsr = Chrome()
brwsr.get(url)
sleep(3)
#1
#TODO: Obter o elemento aside e dele obter as âncoras
aside = brwsr.find_element_by_tag_name('aside')
#TODO: Obter das âncoras um dicionário contendo o nome da ancora(text) e seu link
ancora_aside = aside.find_elements_by_tag_name('a')
d = {d.text: d.get_attribute('href') for d in ancora_aside}
pprint(d)

#2
#TODO: Obter o elemento main e obter as âncoras
main = brwsr.find_element_by_tag_name('main')
#TODO: Obter da ancora o href referênte ao exercício 3 e clicar
ancora_main = main.find_elements_by_tag_name('a')
ancora_main[2].click()