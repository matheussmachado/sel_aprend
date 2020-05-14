"""
OBJETIVO: CHEGAR ATÉ O UNICÓNIO
4 páginas:
- Primeira página = url:
    Clicar para começar -   main -> ancora 

- Segunda página, path = page_1.html:
    Clicar na resposta errada -      main -> ancora de atributo errado -> clicar no href

- Terceira página, path = page_2.html
    * a página demora a responder -> realizar tentativas com laço para obter o text certo
    
    Clicar na resposta certa -      main -> ancora de atr certo -> clicar no href

- Quarta página, path = page_3.html
    clicar na resposta certa -      main -> comparar o href com o path

-Quinta página, path = page_4.html
    dar refresh na página


> Generalizar uma função para obter as ancoras dentro do main
- se o len(ancora) > 0:
    clicar no webElement tal que seu href != diabo.html
  senão:
    dar refresh na pagina  
 

* Realizar um sleep no final da função
* realizar um laço ate o main != None
"""

from selenium.webdriver import Chrome
from time import sleep



url = 'https://selenium.dunossauro.live/exercicio_03.html'
valido = False

def get_elements_by_force(parent, tag):
    """Obter elementos pela força, em virtude do carregamento tardio do DOM

    Arguments:
        parent {webElement} -- um webElement pai
        tag {webElement?} -- a tag do webElement a ser obtido

    Returns:
        list -- uma lista contendo webElements aninhados ao parent
    """
    elements = ''
    elements = parent.find_elements_by_tag_name(tag)
    sleep(1)    
    if 'webelement' in str(elements).lower():
        return elements    
    return get_elements_by_force(parent, tag)

try:
    browser = Chrome()
    browser.get(url)
except:
    print('Não foi possivel conectar')
else:

    while True:        
        sleep(2)
        
        #Aqui ocorre quando chega na última pagina, em que deve-se atualizar a pagina
        if 'page_4' in browser.current_url:
            sleep(5)
            browser.refresh()        
            break

        main = get_elements_by_force(browser, 'main')                                       
        sleep(5)
        ancora = get_elements_by_force(main[0], 'a')        
        
        #Aqui é avaliado o link correto para ir para o próximo passso        
        for a in ancora:
            sleep(1)
            if not 'diabao' in a.get_attribute('href').lower():                
                a.click()
                break        
        del a        