from dataclasses import dataclass, field
from . import markdown_loader
from .bases import DataclassBase, InstanceCollection

BARRIERS = InstanceCollection('id')

@dataclass(repr=False)
class Barrier(DataclassBase):
    id: str
    content: str
    title: str
    driver_id: str
    driver: DataclassBase=None  # type: ignore
    relation_ids: list=field(default_factory=list)
    relations: list=field(default_factory=list)
    changes: list=field(default_factory=list)

    def init(self)-> None:
        self._init_relations()
        self._init_driver()

    def _init_relations(self) -> None:
        for id in self.relation_ids:
            rel = BARRIERS[id]
            self.relations.append(rel)
            rel.relations.append(self)
    
    def _init_driver(self)-> None:
        from .drivers import DRIVERS
        self.driver = DRIVERS[self.driver_id]

for barrier in markdown_loader.filename_to_objs('barriers.md', Barrier):
    BARRIERS.add(barrier)

for barrier in BARRIERS:
    barrier.init()
