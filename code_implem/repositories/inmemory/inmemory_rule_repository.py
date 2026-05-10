from code_implem.repositories.rule_repository import RuleRepository
from code_implem.src.rule import Rule

class InMemoryRuleRepository(RuleRepository):
    def __init__(self):
        self._storage: dict[str, Rule] = {}

    def save(self, entity: Rule) -> None:
        self._storage[entity.rule_id] = entity

    def find_by_id(self, rule_id: str) -> Rule | None:
        return self._storage.get(rule_id)

    def find_all(self) -> list[Rule]:
        return list(self._storage.values())

    def delete(self, rule_id: str) -> None:
        self._storage.pop(rule_id, None)

