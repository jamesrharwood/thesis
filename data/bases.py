from collections import OrderedDict
from dataclasses import dataclass

class InstanceCollection(OrderedDict):
    def __init__(self, index: str, instances: list|None = None):
        instances = instances or []
        self.__index = index
        super().__init__(**self._create_dict(instances))

    def _create_dict(self, instances: list):
        return {self._get_index(i): i for i in instances}
    
    def _get_index(self, obj:type):
        return getattr(obj, self.__index)
    
    def add(self, obj):
        self.update({self._get_index(obj): obj})
    
    def remove(self, index):
        self.pop(index)

    @property
    def _(self):
        return list(self.values())
    
    def __iter__(self):
        return iter(self.values())

class DataclassBase():
    def __repr__(self):
       return f"<{self.__class__.__name__}: {self.id}>"  # type: ignore
