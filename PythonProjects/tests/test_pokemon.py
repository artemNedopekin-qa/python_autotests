import requests
import pytest

host = 	'https://api.pokemonbattle.me:9104'

def test_status_code():
    answer = requests.get(f'{host}/trainers', params = {'trainer_id': 1683})       #Укажи свой id тренера
    assert answer.status_code == 200
    
def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params = {'trainer_id': 1683})  #Укажи свой id тренера
    assert answer_body.json()['trainer_name'] == '[Kansas]Фантазёр'                #Укажи своё имя тренера



@pytest.mark.parametrize('key, value', [('trainer_name', '[Kansas]Фантазёр'),      #Укажи своё имя тренера
                                         ('city', 'Самара'),                       #Укажи свой город, который использовал при регистрации
                                          ('get_history_battle', '0'), 
                                           ('level', '5')])                        #Укажи свой текущий уровень тренера

def test_parts_of_answer(key, value):
    answer = requests.get(f'{host}/trainers', params = {'trainer_id': 1683})       #Укажи свой id тренера
    assert answer.json()[key] == value