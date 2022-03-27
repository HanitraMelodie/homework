#question 2
import requests

list=[150, 151, 5, 29, 23, 25]
with open('pokemon.txt', 'w+') as pokemon_file:
    for i in range(6):
     url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(list[i])
     response = requests.get(url)
     pokemon = response.json()
     name = pokemon['name']
     moves = pokemon['moves']
     pokemon_file.write(f"NAME OF THE POKEMON {name}\n")
     for move in moves:
        move1 = move['move']['name']
        pokemon_file.write(f"{move1}\n")