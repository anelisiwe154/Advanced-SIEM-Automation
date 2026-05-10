
from abc import ABC, abstractmethod
from code_implem.src.rule import Rule
from code_implem.src.incident import Incident

class Processor(ABC):
    @abstractmethod
    def process(self, data):
        pass

class RuleProcessor(Processor):
    def process(self, data):
        return f"Rule processed: {data}"

class IncidentProcessor(Processor):
    def process(self, data):
        return f"Incident processed: {data}"
