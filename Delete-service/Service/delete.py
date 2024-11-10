import os
import sys
from azure.data.tables import TableServiceClient
from azure.storage.blob import BlobServiceClient

table_name = "personas"
container_name = "con-lfaria"

class DeletePersonService:
    table_client = None
    container_client = None
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def __init__(self):
        self.table_client, self.container_client = self.create_client_with_connection_string()

    def create_client_with_connection_string(self):
        if not self.connection_string:
            print("Missing required environment variable for Azure connection string.")
            sys.exit(1)

        # Crear clientes para la tabla y el contenedor
        table_service_client = TableServiceClient.from_connection_string(conn_str=self.connection_string)
        table_client = table_service_client.get_table_client(table_name)

        blob_service_client = BlobServiceClient.from_connection_string(conn_str=self.connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        return table_client, container_client

    def find_row_key_by_id(self, person_id):
        try:
            # Buscar el RowKey correspondiente al ID de la persona
            entities = self.table_client.list_entities()
            for entity in entities:
                if entity.get("id") == person_id:
                    return entity["RowKey"]
            return None
        except Exception as e:
            print(f"Error retrieving entity by id: {e}")
            return None

    def delete_person(self, partition_key, row_key):
        try:
            # Eliminar la entidad de la tabla
            self.table_client.delete_entity(partition_key=partition_key, row_key=row_key)
            print("Person deleted successfully from table.")
            return True
        except Exception as e:
            print(f"Error deleting person from table: {e}")
            return False

    def delete_image(self, blob_name):
        try:
            # Eliminar la imagen del contenedor Blob
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_client.delete_blob()
            print("Image deleted successfully from Blob storage.")
            return True
        except Exception as e:
            print(f"Error deleting image from Blob storage: {e}")
            return False

    def delete_register(self, person_id):
        partition_key = "persona"
        
        # Obtener el RowKey de la persona a eliminar
        row_key = self.find_row_key_by_id(person_id)
        if not row_key:
            print("Delete failed: No matching entity found.")
            return False

        # Eliminar la imagen asociada si existe
        blob_name = f"{partition_key}-{row_key}.jpg"
        self.delete_image(blob_name)

        # Eliminar el registro de la persona en la tabla
        return self.delete_person(partition_key, row_key)
