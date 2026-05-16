from fastapi import APIRouter, HTTPException
from services.rule_service import RuleService, DuplicateRuleException
from code_implem.repositories.inmemory.inmemory_rule_repository import InMemoryRuleRepository
from code_implem.src.rule import Rule
from api.schemas import RuleSchema

router = APIRouter(prefix="/api/rules", tags=["Rules"])
rule_service = RuleService(InMemoryRuleRepository())

@router.get("/", response_model=list[RuleSchema])
def get_all_rules():
    return rule_service.get_rules()

@router.post("/", response_model=RuleSchema)
def add_rule(rule: RuleSchema):
    try:
        return rule_service.add_rule(Rule(**rule.dict()))
    except DuplicateRuleException as e:
        raise HTTPException(status_code=400, detail=str(e))

