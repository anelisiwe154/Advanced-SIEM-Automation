class User:
    def __init__(self, user_id, password, organisation, locale):
        self.user_id = user_id
        self.password = password
        self.organisation = organisation
        self.is_logged_in = False   


    def login(self):
        self.is_logged_in = True
        return f"User {self.user_id} logged in."

    def logout(self):
        self.is_logged_in = False
        return f"User {self.user_id} logged out."

    def view_dashboard(self):
        if not self.is_logged_in:
            raise PermissionError("User must be logged in to view dashboard.")
        return f"{self.organisation} Dashboard for {self.user_id}"