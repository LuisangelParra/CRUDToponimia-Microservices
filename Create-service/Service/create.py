import os
import sys
import uuid
import logging

from azure.data.tables import TableServiceClient, TableEntity
from azure.storage.blob import BlobServiceClient


table_name = "personas"
container_name = "con-lfaria"

class personCreation():

    table_client = None
    container_client = None

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def __init__(self):
        self.table_client, self.container_client = self.create_client_with_connection_string()

    def create_client_with_connection_string(self):
        if self.connection_string is None:
            print("Missing required environment variable(s). Please see specific test for more details." + '\n' + "Test: create_client_with_connection_string")
            sys.exit(1)
        
        # Create a TableServiceClient
        table_service_client = TableServiceClient.from_connection_string(conn_str=self.connection_string)
        table_client = table_service_client.get_table_client(table_name)

        try:
            table_client.create_table()  # Esto solo creará la tabla si no existe
        except:
            logging.info(f"Tabla '{table_name}' ya existe o no es necesario crearla.")
    

        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=self.connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        return table_client, container_client
    
    def insert_image(self, file, blob_name):
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file.stream, overwrite=True)
        imagen_url = blob_client.url
        return imagen_url
    
    def insert_person(self, partition_key, row_key, object):        
        persona = TableEntity()
        persona["PartitionKey"] = partition_key
        persona["RowKey"] = row_key
        persona["typeid"] = object["typeid"]
        persona["id"] = object["id"]
        persona["firstname"] = object["firstname"]
        persona["secondname"] = object["secondname"]
        persona["lastsnames"] = object["lastsnames"]
        persona["birthdate"] = object["birthdate"]
        persona["gender"] = object["gender"]
        persona["email"] = object["email"]
        persona["phone"] = object["phone"]
        persona["imageUrl"] = object["imageUrl"]
        self.table_client.create_entity(entity=persona)

    def save_person(self, object):
        partition_key = "persona"
        row_key = str(uuid.uuid4())
        
        imagen_url = self.insert_image(object["imageUrl"] , f"{partition_key}-{row_key}.jpg")

        object["imageUrl"] = imagen_url

        self.insert_person(partition_key, row_key, object)