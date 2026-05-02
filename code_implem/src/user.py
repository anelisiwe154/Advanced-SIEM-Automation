class User:
    def __init__(self, user_id, password, organisation, locale):
        self.user_id = user_id
        self.password = password
        self.organisation = organisation
        self.locale = locale

    def login(self):
        return f"User {self.user_id} logged in."

    def logout(self):
        return f"User {self.user_id} logged out."

    def view_dashboard(self):
        return f"Dashboard for {self.organisation}."