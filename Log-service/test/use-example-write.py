import requests

url = "https://fa-lg-lfaria.azurewebsites.net/api/writelogs"
data = {
  "typeid": "1",
  "id": "12345",
  "action": "CREATE",
  "details": "New person entry created."
}

response = requests.post(url, data=data)

print(response)