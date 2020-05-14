"""
OBJETIVO: PREENCHER AUTOMATICAMENTE OS DADOS NO FORMULÁRIO E VALIDAR O RESULTADO DA QUERY STRING COM OS DADOS INSERIDO

    - INSERIR OS DADOS:    
        - Criar uma função que busca os webElements, recebe os dados em forma de dicionário e insere no input dos webElements
            
    - OBTER A QUERY DA URL:
        - Pegar a query da current url parseada
        - decodifica a estrutura json gerada pelo resultado
    
    - TESTES UNITÁRIOS: 
        - Testar se o conteúdo do dado foi inserido no input
        - Testar se os dados obtidos 
            - compara a decodificação com os dados inseridos


"""

from selenium.webdriver import Chrome
from time import sleep
from json import loads
from urllib.parse import urlparse


def data_input(brwsr, name_value, keys):
    sleep(1)
    element = brwsr.find_element_by_name(name_value)
    element.send_keys(keys)
    sleep(0.5)
    return element


def query_and_result(brwsr):
    sleep(2)
    queryString = urlparse(brwsr.current_url).query
    queryString = queryString.split('&')[:-1]
    d_query = {
        item.split('=')[0]: item.split('=')[1] for item in queryString
    }
    d_query['email'] = d_query['email'].replace('%40', '@')
    result = brwsr.find_element_by_tag_name('textarea').text
    result = loads(result.replace('\'', "\""))
    return (d_query, result)

