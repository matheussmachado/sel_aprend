"""
- Automatizar o clique até o número sorteado corresponder ao flag.
"""

from time import sleep
from selenium.webdriver import Firefox
import re

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html#'
try:
    browser = Firefox()
    browser.get(url)
except:
    print('Não conectou')
else:
    sleep(5)
    
    #PERCEBI QUE AS VEZES NÃO CONSEGUE ENCONTRAR O ELEMENTO, POR ISSO UM LAÇO ATÉ ENCONTRAR
    while True:
        p = browser.find_elements_by_tag_name('p')
        print('tentativa P: ', p)
        if len(p) > 0:
            break

    #REGEX PARA DESCOBRIR UM DIGITO E OBTER ESSE DIGITO PARA O FLAG
    regexFlag = re.compile(r'(\d){1,}')
    for e in p:        
        flag = regexFlag.search(e.text)
        if flag != None:
            flag = flag.group()
            break
    

    #REGEX DO ULTIMO ELEMENTO GERADO PARA COMPARAR COM O FLAG
    regexUltimo = re.compile(r'(\d){1,}')

    ancora = browser.find_element_by_tag_name('a')

    #FAZER UM LOOP INFINITO DE CLIQUE
    while True:
        ancora.click()
        ultimo = browser.find_elements_by_tag_name('p')[-1]        
        if regexUltimo.search(ultimo.text).group() == flag:        
            break