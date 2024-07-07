import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon_data in pokemon_data_list:
    pokemon_name = pokemon_data['data']
    pokemon_abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    print(f"Name: {pokemon_name}")
    print("Abilities:", ", ".join(pokemon_abilities))

average_weight = calculate_average_weight(pokemon_data_list)
print(f"Average Weight: {average_weight}")