from ex04 import *
import unittest

data = {
    'nome': 'Eduardo',
    'email': 'dudu@du.edu',
    'senha': 'q1w2e3r4',
    'telefone': '987654321',
}

url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = Chrome()
browser.get(url)
sleep(3)

class inputOutputTest(unittest.TestCase):
    
    def test_1(self):    
        elemento = data_input(browser, 'nome', data['nome'])        
        valor = elemento.get_attribute('value')
        self.assertEqual(valor, data['nome'])

    def test_2(self):
        elemento = data_input(browser, 'email', data['email'])
        valor = elemento.get_attribute('value')
        self.assertEqual(valor, data['email'])

    def test_3(self):
        elemento = data_input(browser, 'senha', data['senha'])
        valor = elemento.get_attribute('value')
        self.assertEqual(valor, data['senha'])
    
    def test_4(self):
        elemento = data_input(browser, 'telefone', data['telefone'])
        valor = elemento.get_attribute('value')
        self.assertEqual(valor, data['telefone'])


    def test_5(self):
        browser.find_element_by_name('btn').click()
        sleep(3)
        dict_query, result = query_and_result(browser)
        self.assertEqual(dict_query, result)



if __name__ == '__main__':
    unittest.main(exit=False)
