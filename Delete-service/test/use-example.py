import requests

url = "https://fa-de-lfaria.azurewebsites.net/api/delete"

response = requests.post(url, params={"id": "12346"})

print(response.content)