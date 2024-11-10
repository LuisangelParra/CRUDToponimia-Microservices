# Example Request for getperson Function

Este ejemplo muestra cómo realizar una solicitud a la función `getperson` para obtener los datos de uno o todos los usuarios.

## Obtener un usuario específico

Para obtener los datos de un usuario específico, usa su `id` en el cuerpo de la solicitud.

```bash
curl.exe -X POST "https://fa-rd-lfaria.azurewebsites.net/api/getperson" \
    -H "Content-Type: application/json" \
    -d "{\"id\": \"123\"}"
```

## Obtener todos los usuarios
Para obtener todos los usuarios, omite el parámetro id en el cuerpo de la solicitud.

```bash
curl.exe -X POST "https://fa-rd-lfaria.azurewebsites.net/api/getperson" \
    -H "Content-Type: application/json" \
    -d "{}"
```