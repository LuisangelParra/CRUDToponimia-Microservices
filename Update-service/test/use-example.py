import requests

url = "http://localhost:7071/api/updateperson"
data = {
    "typeid": "1",
    "id": "12346",
    "firstname": "Jhonathan",
    "secondname": "Doe",
    "lastsnames": "Perez",
    "birthdate": "1990-01-01",
    "gender": "M",
    "email": "juan.perez@example.com",
    "phone": "5551234567"
}

response = requests.put(url, data=data)

print(response)
