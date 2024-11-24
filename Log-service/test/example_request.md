# Example Requests for Log Service

The log service allows creating and querying logs.

## Write Log

**URL**: `https://fa-lg-lfaria.azurewebsites.net/api/writelogs`  
**Method**: `POST`

### Request Body

```json
{
  "typeid": "1",
  "id": "12345",
  "action": "CREATE",
  "details": "New person entry created."
}
```

### Example cURL Command:

    ```bash
    curl -X POST "https://fa-lg-lfaria.azurewebsites.net/api/querylogs" \
    -F "typeid": "1" \
    -F "id": "12345" \
    -F "action": "CREATE" \
    -F "details": "New person entry created." 
    ```

## Query Logs
**URL**: `https://fa-log-lfaria.azurewebsites.net/api/querylogs`
**Method**: `POST`

### Query Parameters

| Parameter   | Type   | Required | Description                                     |
|-------------|--------|----------|-------------------------------------------------|
| `typeid`    | string | No       | Filter logs by `typeid`.                       |
| `id`        | string | No       | Filter logs by `id`.                           |
| `from_date` | string | No       | Start date for log query (ISO format).         |
| `to_date`   | string | No       | End date for log query (ISO format).           |


### Example cURL Command:

### Example 1: Query by `typeid` and `id`

    ```bash
    curl -X GET "https://fa-lg-lfaria.azurewebsites.net/api/querylogs" \
    -F "typeid": "1" \
    -F "id": "12345" 
    ```

### Example 2: Query by Date Range

    ```bash
    curl -X GET "https://fa-lg-lfaria.azurewebsites.net/api/querylogs" \
    -F "from_date": "2024-11-10T18:30:32Z" \
    -F "to_date": "2024-11-10T18:30:32Z" 
    ```

### Example Response

```json
[
  {
    "PartitionKey": "log",
    "RowKey": "1699627232.123456",
    "typeid": "1",
    "id": "12345",
    "action": "CREATE",
    "details": "New person entry created.",
    "timestamp": "2024-11-10T18:30:32Z"
  }
]
```
---

Con esto, tienes la implementación completa para la funcionalidad de logs, incluyendo escritura y consulta con filtros.
