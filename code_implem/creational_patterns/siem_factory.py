
from abc import ABC, abstractmethod
from src.alert import Alert
from src.incident import Incident

class SIEMFactory(ABC):
    @abstractmethod
    def create_alert(self, **kwargs):
        pass

    @abstractmethod
    def create_incident(self, **kwargs):
        pass


class CloudSIEMFactory(SIEMFactory):
    def create_alert(self, **kwargs):
        kwargs["category"] = "Cloud"
        return Alert(**kwargs)

    def create_incident(self, **kwargs):
        kwargs["type"] = "Cloud"
        return Incident(**kwargs)


class OnPremSIEMFactory(SIEMFactory):
    def create_alert(self, **kwargs):
        kwargs["category"] = "OnPrem"
        return Alert(**kwargs)

    def create_incident(self, **kwargs):
        kwargs["type"] = "OnPrem"
        return Incident(**kwargs)


