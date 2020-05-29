"""
OBJETIVO: Obter todas as cores da caixinha através de ações de teclado e mouse

- mouse enter no <rect> e realizar uma série de disparos de mouse e teclado e por fim mouse leave

- obter o valor de cor do ultimo json que gera no <textarea>
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
url = 'https://selenium.dunossauro.live/caixinha'

#VERIFICAR O getModifier()



browser = Firefox()
browser.implicitly_wait(30)
browser.get(url)
textarea = browser.find_element_by_tag_name('textarea')
rect = browser.find_element_by_tag_name('rect')

ac = ActionChains(browser)

ac.move_to_element(rect)
ac.pause(3)

ac.click()
ac.pause(3)

ac.double_click()
ac.pause(3)

ac.key_down(Keys.CONTROL)
ac.click()


ac.double_click()
ac.pause(3)

ac.key_down(Keys.SHIFT)
ac.click()
ac.pause(3)

ac.double_click()
ac.pause(3)

ac.key_up(Keys.CONTROL)
ac.click()


ac.double_click()
ac.key_up(Keys.SHIFT)


ac.move_to_element(textarea)
ac.pause(3)

ac.key_down(Keys.CONTROL)
ac.move_to_element(rect)
ac.pause(3)

ac.move_to_element(textarea)
ac.pause(3)

ac.key_down(Keys.SHIFT)
ac.move_to_element(rect)
ac.pause(3)

ac.move_to_element(textarea)
ac.pause(3)

ac.key_up(Keys.CONTROL)
ac.move_to_element(rect)
ac.key_up(Keys.SHIFT)
ac.pause(3)

ac.context_click()
ac.pause(3)

ac.move_to_element(textarea)
ac.pause(3)

ac.perform()

cores = []
string = textarea.text.replace('\"', '')
elements = string.split('\n')
for element in set(elements):
    color = element.split(',')[1]
    color = color.split(':')[-1]
    cores.append(color)

print(len(cores))
print()
print(cores)
print()
print(set(elements))

'''input('pressione a tecla enter...')
browser.quit()
os.system('taskkill /f /im geckodriver.exe')'''