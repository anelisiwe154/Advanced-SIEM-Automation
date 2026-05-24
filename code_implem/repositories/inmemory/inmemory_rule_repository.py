from code_implem.repositories.rule_repository import RuleRepository
from code_implem.src.rule import Rule

class InMemoryRuleRepository(RuleRepository):
    def __init__(self):
        self._storage: dict[str, Rule] = {}

    def save(self, entity: Rule) -> None:
        self._storage[entity.id] = entity

    def find_by_id(self, id: str) -> Rule | None:
        return self._storage.get(id)

    def find_all(self) -> list[Rule]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        self._storage.pop(id, None)

    def find_by_name(self, name: str) -> Rule | None:
        for rule in self._storage.values():
            if rule.name == name:
                return rule
        return None


