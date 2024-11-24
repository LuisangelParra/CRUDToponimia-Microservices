import requests

url = "https://fa-lg-lfaria.azurewebsites.net/api/querylogs"
data = {
  "typeid": "1",
  "id": "12345",
  "from_date": "2024-01-01T00:00:00Z",
  "to_date": "2024-12-31T23:59:59Z"
}

response = requests.post(url, data=data)

print(response.text)