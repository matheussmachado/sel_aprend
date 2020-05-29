import unittest
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)
#REALIZAR ASSERÇÕES DENTRO DA ESCUTA
class Escuta(AbstractEventListener):
    
    def before_click(self, element, webdriver):
        if element.id == 'nome':        
            print(webdriver.find_element_by_id('lnome').text)        
    
    
    def after_click(self, element, webdriver):
        if element.id == 'nome':        
            print(webdriver.find_element_by_id('lnome').text)
        

def get_labels_txt(brows):
    labels = [
        label.text for label in brows.find_elements_by_tag_name('label')[:-1]
        ]
    return labels

url = 'https://selenium.dunossauro.live/exercicio_07'
browser = Firefox()

browser.implicitly_wait(20)

new_driver = EventFiringWebDriver(browser, Escuta())

new_driver.get(url)

#lnome = new_driver.find_element_by_id('lnome')
#lnome.click()
input_nome = new_driver.find_element_by_id('nome')
input_nome.click()
input_nome.send_keys('meu nome')
"""nome = new_driver.find_element_by_name('nome')
nome.send_keys('meu nome')
sleep(2)
email = new_driver.find_element_by_name('email')
email.send_keys('meu@email')
sleep(2)
senha = new_driver.find_element_by_name('senha')
senha.send_keys('senha')
sleep(2)
new_driver.find_element_by_name('btn').click()
"""

'''
- Obter o nome de todos os labels e realizar uma asserção para antes e depois de cada click
'''


'''class Tests(unittest.TestCase):

    def test_1(self):
        #Ao enviar o nome
        nome = new_driver.find_element_by_name('nome')
        nome.send_keys('meu nome')
        self.assertEqual(get_labels_txt(new_driver), ['Não vale mentir o nome', 'email:', 'senha:'])


    def test_2(self):
        email = new_driver.find_element_by_name('email')
        email.send_keys('meu@email')
        self.assertEqual(get_labels_txt(new_driver), ['nome:', 'Esse email é mesmo válido?', 'senha:'])
    
    def test_3(self):
        senha = new_driver.find_element_by_name('senha')
        senha.send_keys('senha')
        self.assertEqual(get_labels_txt(new_driver), ['nome:', 'email:', 'Já falei pra não colocar 1234'])
    
    def test_4(self):
        new_driver.find_element_by_name('btn').click()
        self.assertEqual(get_labels_txt(new_driver), ['nome:', 'email:', 'senha:'])


if __name__ == '__main__':
    unittest.main()'''

browser.quit()