import requests

token = 'Укажи свой токен'
host = 	'https://api.pokemonbattle.me:9104'

answer = requests.post(f'{host}/pokemons', json =
                       
    {
    "name": "Бабайка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"trainer_token": token, "Content-Type": "application/json"})

print(answer.text)

answer_name = requests.put(f'{host}/pokemons', json =
                       
    {
    "pokemon_id": "10727",
    "name": "Бабайка с лопатой",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
, headers = {"trainer_token": token, "Content-Type": "application/json"})

print(answer_name.text)



answer_caught = requests.post(f'{host}/trainers/add_pokeball', json =
                       
    {
    "pokemon_id": "10727"
}
, headers = {"trainer_token": token, "Content-Type": "application/json"})

print(answer_caught.text)