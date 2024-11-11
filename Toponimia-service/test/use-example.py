import requests

url = "https://fa-tp-lfaria.azurewebsites.net/api/toponimia"

response = requests.get(url, params={"firstname": "juan"})

print(response.content)