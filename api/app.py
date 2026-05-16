from fastapi import FastAPI
from api import incidents, alerts, rules, users

app = FastAPI(title="SIEM API", version="1.0")

app.include_router(incidents.router)
app.include_router(alerts.router)
app.include_router(rules.router)
app.include_router(users.router)

