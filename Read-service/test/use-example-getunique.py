import requests

url = "https://fa-rd-lfaria.azurewebsites.net/api/getperson"

response = requests.get(url, params={"id": "12346"})

print(response.content)