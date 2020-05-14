from selenium.webdriver import Firefox

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if text in elemento.text:
            return elemento

def find_by_href(browser, link):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.href:
            return elemento

url = 'http://selenium.dunossauro.live/aula_04_a.html'
brwsr = Firefox()
brwsr.get(url)