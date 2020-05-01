from time import sleep
from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()
browser.get(url)
sleep(30)
p = browser.find_element_by_tag_name('p')
print(p.text)
browser.quit()