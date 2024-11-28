import os
import sys
from azure.data.tables import TableServiceClient, TableEntity
import datetime

log_table_name = "logs"

class LogService:
    table_client = None
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    def __init__(self):
        self.table_client = self.create_table_client()

    def create_table_client(self):
        if self.connection_string is None:
            print("Missing required environment variable(s). Please set 'AZURE_STORAGE_CONNECTION_STRING'.")
            sys.exit(1)

        table_service_client = TableServiceClient.from_connection_string(conn_str=self.connection_string)
        table_client = table_service_client.get_table_client(log_table_name)
        
        return table_client

    def write_log(self, log_data):
        try:
            # Add a timestamp to the log entry
            log_entity = TableEntity()
            log_entity["PartitionKey"] = "log"
            
            #row key
            log_entity["RowKey"] = log_data["id"]+"-"+str(datetime.datetime.now())

            log_entity["id"] = log_data["id"]
            log_entity["typeid"] = log_data["typeid"]
            log_entity["action"] = log_data["action"]
            log_entity["details"] = log_data["details"]

            self.table_client.create_entity(entity=log_entity)
            print("Log entry written successfully.")
        except Exception as e:
            print(f"Error writing log: {e}")

    def query_logs(self, filters):
        try:
            # Build filter string dynamically based on provided filters
            filter_clauses = []
            if "typeid" in filters and filters["typeid"] is not None:
                filter_clauses.append(f"typeid eq '{filters['typeid']}'")
            if "id" in filters and filters["id"] is not None:
                filter_clauses.append(f"id eq '{filters['id']}'")
            if "from_date" in filters and filters["from_date"] is not None:
                filter_clauses.append(f"Timestamp ge datetime'{filters['from_date']}'")
            if "to_date" in filters and filters["to_date"] is not None:
                filter_clauses.append(f"Timestamp le datetime'{filters['to_date']}'")

            filter_expression = " and ".join(filter_clauses) if filter_clauses else None

            logs = self.table_client.query_entities(query_filter=filter_expression)
            return [log for log in logs]
        except Exception as e:
            print(f"Error querying logs: {e}")
            return None
