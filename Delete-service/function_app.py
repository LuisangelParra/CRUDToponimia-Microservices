import azure.functions as func
from Service.delete import DeletePersonService
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Endpoint para eliminar un registro de persona
@app.route("delete", methods=["POST"])
def delete(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Obtener el ID de la persona a eliminar desde el cuerpo de la solicitud
        person_id = req.params.get('id')

        if not person_id:
            return func.HttpResponse(
                "Please pass a person 'id' in the request body",
                status_code=400
            )

        # Crear una instancia del servicio de eliminación y realizar la operación
        delete_service = DeletePersonService()
        result = delete_service.delete_register(person_id)

        if result:
            return func.HttpResponse(
                json.dumps({"message": "Person deleted successfully"}),
                status_code=200,
                mimetype="application/json"
            )
        else:
            return func.HttpResponse(
                "Person not found or could not be deleted",
                status_code=404
            )

    except Exception as e:
        return func.HttpResponse(
            f"Error deleting person: {e}",
            status_code=500
        )
