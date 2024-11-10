import requests

url = "https://fa-cr-lfaria.azurewebsites.net/api/create"
data = {
    "typeid": "1",
    "id": "12346",
    "firstname": "Jhon",
    "secondname": "Doe",
    "lastsnames": "Perez",
    "birthdate": "1990-01-01",
    "gender": "M",
    "email": "juan.perez@example.com",
    "phone": "5551234567"
}

files = {
    "imageUrl": open("test.jpg", "rb")
}

response = requests.post(url, data=data, files=files)

print(response.text)
