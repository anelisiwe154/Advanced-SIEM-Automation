class User:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.user_id = id   # alias for repository compatibility
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        return f"User {self.id} deactivated."

