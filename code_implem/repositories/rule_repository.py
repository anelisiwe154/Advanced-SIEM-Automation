
from typing import Optional, List
from .repository import Repository
from code_implem.src.rule import Rule

class RuleRepository(Repository[Rule, str]):
    def save(self, entity: Rule) -> None:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Optional[Rule]:
        raise NotImplementedError

    def find_all(self) -> List[Rule]:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
