
from abc import ABC, abstractmethod

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
