import requests
import logging

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            pokeman_data = response.json()
            return pokeman_data
        else:
            print(f"Failed to retrieve data {response.status_code}")
    except Exception as err:
        logging.error(f"An unexpected error occurred: {err}")
    finally:
        print("Request attempt finished!!!")
    
pokeman_name = "pikachu"
pokeman_info = get_pokemon_info(pokeman_name)

if pokeman_info:
    print(f"{pokeman_info['name']}")
