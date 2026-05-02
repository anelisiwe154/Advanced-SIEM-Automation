
class DatabaseConnection:
    _instance = None

    def __new__(cls, connection_string=None):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection_string = connection_string
        return cls._instance

    def connect(self):
        return f"Connected to {self.connection_string}"
