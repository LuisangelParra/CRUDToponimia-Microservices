import azure.functions as func
import logging
import Service.read as read

import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route('getperson', methods=['GET'])
def get_user(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request to get user data.")

    user_id = req.params.get('id')
    
    response = read.personRead()

    if user_id:
        # Consultar un solo registro usando el id
        user = response.get_person(user_id)
        if user:
            return func.HttpResponse(json.dumps(user), status_code=200, mimetype="application/json")
        else:
            return func.HttpResponse("User not found", status_code=404)
    else:
        # Consultar todos los registros
        users = response.get_all_persons()
        print(users)
        if users:
            return func.HttpResponse(json.dumps(users), status_code=200, mimetype="application/json")
        else:
            return func.HttpResponse("No users found", status_code=404)


