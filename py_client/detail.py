import requests

endpoint = "http://127.0.0.1:8000/api/products/1/" #http://127.0.0.1:8000/

get_response = requests.get(endpoint) # HTTP Request

print(get_response.json())
