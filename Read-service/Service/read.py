import os
import sys

from azure.data.tables import TableServiceClient, TableEntity

table_name = "personas"

class personRead():
    table_client = None
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def __init__(self):
        self.table_client = self.create_client_with_connection_string()

    def create_client_with_connection_string(self):
        if self.connection_string is None:
            print("Missing required environment variable(s). Please see specific test for more details." + '\n' + "Test: create_client_with_connection_string")
            sys.exit(1)
        
        # Create a TableServiceClient
        table_service_client = TableServiceClient.from_connection_string(conn_str=self.connection_string)
        table_client = table_service_client.get_table_client(table_name)

        return table_client

    def get_person(self, id):
        filter_query = f"id eq '{id}'"
        try:
            entities = self.table_client.query_entities(filter_query)
            personas = [entity for entity in entities]
            # Si la búsqueda fue exitosa y encontró al menos un usuario, devolver el primer resultado
            if personas:
                return personas[0]
            else:
                return None
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None
    
    def get_all_persons(self):
        try:
            personas = self.table_client.list_entities()
            return [persona for persona in personas]
        except Exception as e:
            print(f"Error retrieving all users: {e}")
            return None