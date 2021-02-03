"""
aguardar e interagir com o botão até aparecer a classe abaixo no botão:
btn btn-primary btn-ghost selenium

- esperar o botão: se direcionar até o botão pelo id
- esperar o a classe .selenium
"""

from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def esperar_elemento(by, query, webdriver):
    elements = webdriver.find_elements(by, query)
    if elements:
        print(f"{elements[0].text} apareceu!")
        return True
    return False

def esperar_classe_selenium(webdriver):
    element = webdriver.find_element_by_css_selector("[class$=selenium]")
    if element:
        print(f"{element.text} apareceu. Classe: {element.get_attribute('class')}")
        return True
    return False


f = Firefox()

kwargs_1 = dict(
    by=By.ID,
    query= 'request'
    
)
'''
kwargs_2 = dict(
    by=By.CSS_SELECTOR,
    query='selenium'   
)'''

url = 'https://selenium.dunossauro.live/exercicio_09.html'

f.get(url)

wdw = WebDriverWait(f, timeout=30)
wdw.until(esperar_classe_selenium)

