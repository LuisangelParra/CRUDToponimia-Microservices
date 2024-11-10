### `example_request.md`

## Eliminar un registro de persona

### Descripción
Este endpoint permite eliminar un registro de persona en la base de datos, así como su imagen asociada en el almacenamiento de blobs (si existe). La eliminación se realiza a partir del `id` de la persona.

### URL
`POST https://fa-de-lfaria.azurewebsites.net/api/delete`

### Formato de solicitud
La solicitud debe enviarse en formato JSON e incluir el campo `id` de la persona a eliminar.

### Encabezados requeridos
- `Content-Type: application/json`

### Cuerpo de la solicitud
```json
{
  "id": "12346"
}
```

### Ejemplo de uso con `curl`

```bash
curl -X POST "https://fa-de-lfaria.azurewebsites.net/api/delete" \
  -H "Content-Type: application/json" \
  -d '{
        "id": "12346"
      }'
```

### Respuestas

#### Éxito
Si el registro se elimina con éxito:
```json
{
  "message": "Person deleted successfully"
}
```
**Código de estado:** `200 OK`

#### Error - Persona no encontrada
Si no se encuentra el registro correspondiente al `id`:
```json
{
  "error": "Person not found or could not be deleted"
}
```
**Código de estado:** `404 Not Found`

#### Error - Fallo en la eliminación
Si ocurre un error durante la eliminación:
```json
{
  "error": "Error deleting person: <detalles_del_error>"
}
```
**Código de estado:** `500 Internal Server Error`

---
