

# Example Request for Toponymy Function

The `toponimia` function retrieves the origin of a given name based on toponymy. Use this endpoint to get historical and geographical background related to a specified name.

## Endpoint
**URL**: `https://fa-tp-lfaria.azurewebsites.net/api/toponimia`

**Method**: `GET`

## Request Parameters

| Parameter  | Type   | Required | Description                             |
|------------|--------|----------|-----------------------------------------|
| firstname  | string | Yes      | The name for which to retrieve toponymy information. |

## Example Requests

### Example 1: Retrieve Toponymy for a Name

Request the toponymic origin of the name "Juan":

```bash
curl -X GET "https://fa-tp-lfaria.azurewebsites.net/api/toponimia?firstname=Juan"
```

#### Response

```json
{
  "toponimy_origin": "The name 'Juan' originates from the Hebrew name Yochanan, meaning 'God is gracious.' It became popular in Spain and Latin America, often associated with historic figures and saints."
}
```

### Example 2: Retrieve Toponymy for a Different Name

Request the toponymic origin of the name "Maria":

```bash
curl -X GET "https://fa-tp-lfaria.azurewebsites.net/api/toponimia?firstname=Maria"
```

#### Response

```json
{
  "toponimy_origin": "The name 'Maria' is derived from the Hebrew name Miriam. It holds significant cultural and religious importance across various countries, particularly in Christian and Spanish-speaking communities."
}
```

## Error Responses

If the required parameter `firstname` is missing, the response will indicate an error.

### Example Error

```bash
curl -X GET "https://fa-tp-lfaria.azurewebsites.net/api/toponimia"
```

#### Response

```json
{
  "error": "Please provide a 'firstname' parameter."
}
```
