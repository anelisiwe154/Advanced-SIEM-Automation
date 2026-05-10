from code_implem.repositories.inmemory.inmemory_alert_repository import InMemoryAlertRepository
from code_implem.repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from code_implem.repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from code_implem.repositories.inmemory.inmemory_rule_repository import InMemoryRuleRepository

from code_implem.repositories.database.database_alert_repository import DatabaseAlertRepository
from code_implem.repositories.filesystem.filesystem_alert_repository import FileSystemAlertRepository


class RepositoryFactory:
    @staticmethod
    def get_repository(entity_type: str, storage_type: str):
        storage_type = storage_type.upper()
        entity_type = entity_type.upper()

        if storage_type == "MEMORY":
            if entity_type == "ALERT":
                return InMemoryAlertRepository()
            elif entity_type == "INCIDENT":
                return InMemoryIncidentRepository()
            elif entity_type == "USER":
                return InMemoryUserRepository()
            elif entity_type == "RULE":
                return InMemoryRuleRepository()
            else:
                raise ValueError(f"Unknown entity type: {entity_type}")

        elif storage_type == "DATABASE":
            if entity_type == "ALERT":
                return DatabaseAlertRepository("db://connection-string")
            else:
                raise ValueError(f"Unknown entity type for DATABASE: {entity_type}")

        elif storage_type == "FILESYSTEM":
            if entity_type == "ALERT":
                return FileSystemAlertRepository("alerts.json")
            else:
                raise ValueError(f"Unknown entity type for FILESYSTEM: {entity_type}")

        else:
            raise ValueError(f"Invalid storage type: {storage_type}")


        
