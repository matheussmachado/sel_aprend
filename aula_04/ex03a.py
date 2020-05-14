from selenium.webdriver import Chrome
from time import sleep



url = 'https://selenium.dunossauro.live/page_2.html'

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
        print('passou')
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
            print('passou por aqui')
            break

        main = get_elements_by_force(browser, 'main')                                       
        sleep(5)
        ancora = get_elements_by_force(main[0], 'a')        
        
        #Aqui é avaliado o link correto para ir para o próximo passso        
        for a in ancora:
            sleep(1)
            #diabao in a.lower()
            if not 'diabao' in a.get_attribute('href').lower():                
                a.click()
                print('indo pra page 3')                                        
                break
        
        del a
        print('ultima linha')