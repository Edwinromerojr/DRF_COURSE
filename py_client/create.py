import requests


headers = {'Authorization': 'Bearer c6d6fe1583b002da47ea7c1ff4c4a912ae68d5a6'}
endpoint = "http://127.0.0.1:8000/api/products/" #http://127.0.0.1:8000/

data = {
    "title": "This field is done",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers) # HTTP Request

print(get_response.json())
