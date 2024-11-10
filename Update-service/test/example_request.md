Aquí tienes el archivo `example_request.md` para la URL `https://fa-up-lfaria.azurewebsites.net/api/updateperson`, que incluye ejemplos para peticiones con y sin imagen.

---

# Example Request for Updating a Person

## URL

**Endpoint:** `https://fa-up-lfaria.azurewebsites.net/api/updateperson`

## Description

Este endpoint permite actualizar la información de un registro de persona en la base de datos de Azure Table Storage. Si se proporciona una nueva imagen, reemplaza la imagen existente en el Blob Storage y actualiza el enlace a la imagen en el registro.

---

## Request Headers

- `Content-Type: multipart/form-data`

---

## Request Parameters

| Parameter   | Type   | Required | Description                             |
|-------------|--------|----------|-----------------------------------------|
| `typeid`    | String | Yes      | Tipo de identificación de la persona.   |
| `id`        | String | Yes      | ID único de la persona a actualizar.    |
| `firstname` | String | Yes      | Nombre de la persona.                   |
| `secondname`| String | No       | Segundo nombre de la persona.           |
| `lastsnames`| String | Yes      | Apellidos de la persona.                |
| `birthdate` | String | Yes      | Fecha de nacimiento (formato `YYYY-MM-DD`). |
| `gender`    | String | Yes      | Género de la persona.                   |
| `email`     | String | Yes      | Email de la persona.                    |
| `phone`     | String | Yes      | Teléfono de la persona.                 |
| `imageUrl`  | File   | No       | Archivo de imagen opcional para actualizar la foto de la persona. |

---

## Example Requests

### Request with Image

```bash
curl -X POST "https://fa-up-lfaria.azurewebsites.net/api/updateperson" \
    -F "typeid=1" \
    -F "id=12346" \
    -F "firstname=Jhon" \
    -F "secondname=Doe" \
    -F "lastsnames=Pérez" \
    -F "birthdate=1990-01-01" \
    -F "gender=M" \
    -F "email=juan.perez@example.com" \
    -F "phone=5551234567" \
    -F "imageUrl=@./path/to/your/image.png"
```

### Request without Image

```bash
curl -X POST "https://fa-up-lfaria.azurewebsites.net/api/updateperson" \
    -F "typeid=1" \
    -F "id=12346" \
    -F "firstname=Jhon" \
    -F "secondname=Doe" \
    -F "lastsnames=Pérez" \
    -F "birthdate=1990-01-01" \
    -F "gender=M" \
    -F "email=juan.perez@example.com" \
    -F "phone=5551234567"
```

---

## Response

- **200 OK** - Si la actualización fue exitosa.
- **400 Bad Request** - Si falta algún parámetro requerido o el formato es incorrecto.
- **500 Internal Server Error** - Si ocurre un error en el servidor.

### Example Successful Response

```json
{
  "message": "Person updated successfully",
  "updatedPerson": {
    "PartitionKey": "persona",
    "RowKey": "46ddd48b-df6f-4491-9c83-88a6739af881",
    "typeid": "1",
    "id": "12346",
    "firstname": "Jhon",
    "secondname": "Doe",
    "lastsnames": "Pérez",
    "birthdate": "1990-01-01",
    "gender": "M",
    "email": "juan.perez@example.com",
    "phone": "5551234567",
    "imageUrl": "https://your_blob_storage_url/container_name/filename.png"
  }
}
```

--- 

Este archivo proporciona un ejemplo claro y detallado para interactuar con el endpoint de actualización, tanto con imagen como sin imagen.