from pydantic import BaseModel, ConfigDict

class RuleSchema(BaseModel):
    id: str
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class IncidentSchema(BaseModel):
    id: str
    description: str
    is_escalated: bool = False
    is_acknowledged: bool = False

    model_config = ConfigDict(from_attributes=True)

class AlertSchema(BaseModel):
    id: str
    description: str
    is_acknowledged: bool = False
    is_dismissed: bool = False

    model_config = ConfigDict(from_attributes=True)

class UserSchema(BaseModel):
    id: str
    name: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


