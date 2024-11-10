import azure.functions as func
import logging
import Service.update as register

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route('updateperson', methods=['PUT'])
def update(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    data = {
        "typeid": req.form["typeid"],
        "id": req.form["id"],
        "firstname": req.form["firstname"],
        "secondname": req.form["secondname"],
        "lastsnames": req.form["lastsnames"],
        "birthdate": req.form["birthdate"],
        "gender": req.form["gender"],
        "email": req.form["email"],
        "phone": req.form["phone"],
        "imageUrl": req.files["imageUrl"] if "imageUrl" in req.files else None,
    }

    # Validate data
    for key in data:
        if key == "imageUrl":
            continue
        if data[key] == "":
            return func.HttpResponse(f"Please provide {key} field", status_code=400)
        
    response = register.personUpdate()
    response.update_register(data)
    logging.info("Person updated")
    return func.HttpResponse("Person updated", status_code=200)