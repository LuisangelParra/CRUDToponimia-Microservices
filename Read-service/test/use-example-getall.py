import requests

url = "https://fa-rd-lfaria.azurewebsites.net/api/getperson"

response = requests.get(url)

print(response.content)