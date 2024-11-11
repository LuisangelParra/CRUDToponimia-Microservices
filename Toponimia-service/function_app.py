import os
from openai import OpenAI
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)



class NameToponymy:
    def __init__(self):
        pass
    
    # Configurar la clave de API de OpenAI
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")

    def generate_toponimia(self, firstname):
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f'Origen del nombre "{firstname}" según la toponimia.'}],
        )
        return response.choices[0].message.content

# Instanciar la clase
name_toponymy = NameToponymy()

# Crear el endpoint en function_app.py
@app.route('toponimia', methods=['GET'])
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Obtener el nombre de la solicitud
        firstname = req.params.get("firstname")
        if not firstname:
            return func.HttpResponse(
                "Por favor, proporciona un nombre en el parámetro 'firstname'.",
                status_code=400
            )
        
        # Llamar a la función para obtener el origen toponímico
        toponimia = name_toponymy.generate_toponimia(firstname)
        
        # Retornar la respuesta de OpenAI
        return func.HttpResponse(toponimia, status_code=200)

    except Exception as e:
        return func.HttpResponse(
            f"Error al generar la toponimia del nombre: {e}",
            status_code=500
        )
