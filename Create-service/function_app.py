import azure.functions as func
import logging
import Service.create as register
import azure.identity as DefaultAzureCredential

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route("create", methods=["POST"])
def create(req: func.HttpRequest) -> func.HttpResponse:
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
        "imageUrl": req.files["imageUrl"],
    }

    # Validate data
    for key in data:
        if data[key] == "":
            return func.HttpResponse(f"Please provide {key} field", status_code=400)

    response = register.personCreation()
    response.save_person(data)

    logging.info("Person created")
    return func.HttpResponse("Person created", status_code=200)