from pydantic import BaseModel

class RuleSchema(BaseModel):
    id: str
    name: str
    description: str | None = None
    class Config: 
        from_attributes = True   # instead of orm_mode

class IncidentSchema(BaseModel):
    id: str
    description: str
    is_escalated: bool = False
    is_acknowledged: bool = False
    class Config: 
        from_attributes = True

class AlertSchema(BaseModel):
    id: str
    description: str
    is_acknowledged: bool = False
    is_dismissed: bool = False
    class Config: 
        from_attributes = True

class UserSchema(BaseModel):
    id: str
    name: str
    is_active: bool = True
    class Config: 
        from_attributes = True

