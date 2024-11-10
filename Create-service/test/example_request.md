# Ejemplo de petición a la API

Este archivo documenta cómo realizar una petición POST a la función `create` que se ejecuta localmente en Azure Functions. La petición incluye datos de una persona y una imagen adjunta.

### Requisitos
- Tener `curl` instalado en tu sistema.
- Ejecutar el Azure Function localmente en `http://localhost:7071/api/create`.
- URL de la Azure Function desplegada en Azure `https://fa-cr-lfaria.azurewebsites.net/api/create`.

### Ejemplo de Petición

Utiliza el siguiente comando `curl` para realizar la petición. Asegúrate de reemplazar los valores de ejemplo según sea necesario.

```bash
curl.exe -X POST "http://localhost:7071/api/create" \
    -F "typeid=1" \
    -F "id=123" \
    -F "firstname=John" \
    -F "secondname=Doe" \
    -F "lastsnames=Smith" \
    -F "birthdate=1990-01-01" \
    -F "gender=M" \
    -F "email=Johndoe@mail.com" \
    -F "phone=1234567890" \
    -F "imageUrl=@./test/test.jpg"
```