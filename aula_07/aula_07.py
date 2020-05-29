from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)

class Escuta(AbstractEventListener):
    
    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':        
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'antes do click no elemento {elemento.tag_name}')
    
    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':        
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'antes do click no elemento {elemento.tag_name}')
        

browser = Firefox()
new_driver = EventFiringWebDriver(browser, Escuta())
new_driver.get('https://selenium.dunossauro.live/aula_07_d')
input_de_texto = new_driver.find_element_by_tag_name('input')
span = new_driver.fint_element_by_tag_name('span')
p = new_driver.fint_element_by_tag_name('p')

browser.quit()