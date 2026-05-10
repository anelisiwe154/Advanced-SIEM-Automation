
import copy
from code_implem.src.alert import Alert

class AlertPrototype:
    def __init__(self):
        self._prototypes = {}

    def register(self, name, alert):
        self._prototypes[name] = alert

    def clone(self, name, **kwargs):
        if name not in self._prototypes:
            raise ValueError("Prototype not found")
        obj = copy.deepcopy(self._prototypes[name])
        obj.__dict__.update(kwargs)
        return obj
