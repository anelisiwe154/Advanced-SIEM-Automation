
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")   
ID = TypeVar("ID") 

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> None:
        """Create or update an entity"""
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Read entity by ID"""
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Read all entities"""
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete entity by ID"""
        pass
