import azure.functions as func
from Service.log import LogService
import json
import logging


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

log_service = LogService()

@app.route('writelogs', methods=['POST'])
def write_log(req: func.HttpRequest) -> func.HttpResponse:
    try:
        log_data = {
            "typeid": req.form["typeid"],
            "id": req.form["id"],
            "action": req.form["action"],
            "details": req.form["details"],
        }

        log_service.write_log(log_data)
        return func.HttpResponse("Log entry created successfully.", status_code=201)
    except Exception as e:
        return func.HttpResponse(f"Error writing log: {e}", status_code=500)

@app.route('querylogs', methods=['POST'])
def query_logs(req: func.HttpRequest) -> func.HttpResponse:
    try:
        filters = {
            "typeid": req.form["typeid"] if "typeid" in req.form else None,
            "id": req.form["id"] if "id" in req.form else None,
            "from_date": req.form["from_date"] if "from_date" in req.form else None,
            "to_date": req.form["to_date"] if "to_date" in req.form else None,
        }
        logs = log_service.query_logs(filters)
        if logs:
            return func.HttpResponse(json.dumps(logs), status_code=200, mimetype="application/json")
        else:
            return func.HttpResponse("No logs found.", status_code=404)
    except Exception as e:
        return func.HttpResponse(f"Error querying logs: {e}", status_code=500)
