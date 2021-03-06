# -*- coding: utf-8 -*-
"""pokedex_brianic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IT2RH89WMoS2EnH6x4BYMxE3XPwEE4RG
"""

import requests

while True:
  try:
    pokemon = input("Masukkan nama Pokemon: ").lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = requests.get(url)
    pokedex = req.json()
  except ValueError:        # including JSONDecodeError "https://github.com/simplejson/simplejson/blob/v3.0.5/simplejson/decoder.py#L33"
    print("Tolong masukkan nama yang benar!")
  else:
    break                   # kalau ga nemu error, brenti looping-nya

# print(pokedex)
print('\n')
print("==== SELAMAT DATANG DI POKEDEX ====")
print(f"Nama Pokemon: {pokedex['name'].capitalize()}")
print(f"HP: {pokedex['stats'][0]['base_stat']}")
print(f"Attack: {pokedex['stats'][1]['base_stat']}")
print(f"Defense: {pokedex['stats'][2]['base_stat']}")
print(f"Speed: {pokedex['stats'][5]['base_stat']}")
print(f"Type: {pokedex['types'][0]['type']['name']}")
print(f"URL Gambar {pokedex['name'].capitalize()}: {pokedex['sprites']['front_default']} ")
print("Abilities:", 
      f"{' '*2}1. {pokedex['abilities'][0]['ability']['name']}", 
      f"{' '*2}2. {pokedex['abilities'][1]['ability']['name']}", 
      sep = '\n')