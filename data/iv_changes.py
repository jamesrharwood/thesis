from dataclasses import dataclass, field
from operator import attrgetter

from . import markdown_loader
from .bases import DataclassBase, InstanceCollection
from .stages import STAGES

CHANGES = InstanceCollection('id')
stages = list(STAGES.keys())

@dataclass(repr=False)
class Change(DataclassBase):
    id: str
    content: str
    title: str
    stage: str
    stage_index = int
    barrier_ids: list
    barriers: list=field(default_factory=list)
    intervention_fn_ids: list=field(default_factory=list)
    intervention_fns: list=field(default_factory=list)
    relation_ids: list=field(default_factory=list)
    relations: list=field(default_factory=list)
    stakeholder_ids: list=field(default_factory=list)
    stakeholders: list=field(default_factory=list)

    def init(self)-> None:
        # register objects from ids
        self._init_barriers()
        self._init_intervention_fns()
        self._init_relations()
        self._init_stakeholders()
        self.stage_index = stages.index(self.stage)

    def _init_barriers(self)-> None:
        from .barriers import BARRIERS
        for barrier_id in self.barrier_ids:
            barrier = BARRIERS[barrier_id]
            self.barriers.append(barrier)
            barrier.changes.append(self)
    
    def _init_intervention_fns(self)-> None:
        from .intervention_fns import INTERVENTION_FNS
        self.intervention_fns = [INTERVENTION_FNS[id] for id in self.intervention_fn_ids]

    def _init_stakeholders(self)-> None:
        from .stakeholders import STAKEHOLDERS
        self.stakeholders = [STAKEHOLDERS[id] for id in self.stakeholder_ids]

    def _init_relations(self) -> None:
        for id in self.relation_ids:
            rel =  CHANGES[id]
            self.relations.append(rel)
            rel.relations.append(self)
    

for change in markdown_loader.filename_to_objs('iv_changes.md', Change):
    CHANGES.add(change)

for change in CHANGES:
    change.init()

CHANGES_BY_STAGE = sorted(CHANGES.values(), key=attrgetter('stage_index'))




