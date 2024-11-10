import os
import sys

from azure.data.tables import TableServiceClient, TableEntity
from azure.storage.blob import BlobServiceClient

table_name = "personas"
container_name = "con-lfaria"

class personUpdate():
    table_client = None
    container_client = None
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def __init__(self):
        self.table_client, self.container_client = self.create_client_with_connection_string()

    def create_client_with_connection_string(self):
        if self.connection_string is None:
            print("Missing required environment variable(s). Please see specific test for more details." + '\n' + "Test: create_client_with_connection_string")
            sys.exit(1)
        
        # Create Table and Blob clients
        table_service_client = TableServiceClient.from_connection_string(conn_str=self.connection_string)
        table_client = table_service_client.get_table_client(table_name)
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=self.connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        return table_client, container_client

    def update_image(self, file, blob_name_base):
        try:
            # Detectar la extensión del archivo subido (.jpg, .png, etc.)
            _, file_extension = os.path.splitext(file.filename)
            blob_name = f"{blob_name_base}{file_extension}"
            
            # Subir la nueva imagen
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_client.upload_blob(file.stream, overwrite=True)
            image_url = blob_client.url
            return image_url
        except Exception as e:
            print(f"Error updating image: {e}")
            return None

    def update_person(self, partition_key, row_key, updates):
        try:
            # Retrieve the existing entity
            entity = self.table_client.get_entity(partition_key=partition_key, row_key=row_key)

            # Apply updates
            for key, value in updates.items():
                entity[key] = value

            # Delete and recreate the entity
            self.table_client.delete_entity(partition_key=partition_key, row_key=row_key)
            self.table_client.create_entity(entity=entity)
            print("Person updated successfully by recreating entity.")
        except Exception as e:
            return f"Error updating person: {e}"


    def find_row_key_by_id(self, person_id):
        try:
            # Obtener todas las entidades y filtrar en el código
            entities = self.table_client.list_entities()
            for entity in entities:
                if entity.get("id") == person_id:
                    return entity["RowKey"]
            print(f"No entity found with id: {person_id}")
            return None
        except Exception as e:
            print(f"Error retrieving entity by id: {e}")
            return None



    def update_register(self, person_data):
        partition_key = "persona"
        person_id = person_data["id"]

        # Buscar el row_key por id
        row_key = self.find_row_key_by_id(person_id)
        print(f"Row key encontrado: {row_key}")
        if not row_key:
            print("Actualización fallida: No se encontró ninguna entidad coincidente.")
            return

        # Verificar entidad existente antes de la actualización
        existing_entity = self.table_client.get_entity(partition_key=partition_key, row_key=row_key)
        print(f"Entidad antes de la actualización: {existing_entity}")

        # Actualizar la imagen si se proporciona una nueva
        if "imageUrl" in person_data and person_data["imageUrl"]:
            blob_name_base = f"{partition_key}-{row_key}"
            new_image_url = self.update_image(person_data["imageUrl"], blob_name_base)
            person_data["imageUrl"] = new_image_url if new_image_url else person_data["imageUrl"]

            # Detalles de la persona para actualizar en la tabla
            updates = {
                "typeid": person_data["typeid"],
                "id": person_data["id"],
                "firstname": person_data["firstname"],
                "secondname": person_data["secondname"],
                "lastsnames": person_data["lastsnames"],
                "birthdate": person_data["birthdate"],
                "gender": person_data["gender"],
                "email": person_data["email"],
                "phone": person_data["phone"],
                "imageUrl": person_data["imageUrl"]
            }
        else:
            # Detalles de la persona para actualizar en la tabla
            updates = {
                "typeid": person_data["typeid"],
                "id": person_data["id"],
                "firstname": person_data["firstname"],
                "secondname": person_data["secondname"],
                "lastsnames": person_data["lastsnames"],
                "birthdate": person_data["birthdate"],
                "gender": person_data["gender"],
                "email": person_data["email"],
                "phone": person_data["phone"]
            }

        # Actualizar persona en la tabla
        self.update_person(partition_key, row_key, updates)

        # Confirmar entidad después de la actualización
        updated_entity = self.table_client.get_entity(partition_key=partition_key, row_key=row_key)
        print(f"Entidad después de la actualización: {updated_entity}")