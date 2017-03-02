import json
from random import randint
import requests

url = 'https://api-fruit.herokuapp.com/api/fruits'

with open('data.json') as data_file:
    data = json.load(data_file)

for fruit in data["fruits"]:
    data = { "name": fruit, "price": randint(1,35) }
    response = requests.post(url, json=data)

