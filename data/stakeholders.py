import yaml

from .bases import InstanceCollection, DataclassBase
from .drivers import Driver
from dataclasses import dataclass, field

STAKEHOLDERS = InstanceCollection('id')

@dataclass(repr=False)
class Stakeholder(DataclassBase):
    id: str
    title: str
    colour: str
    description: str
    policy_category_ids: list
    policy_categories: list=field(default_factory=list)

    def init(self)-> None:
        self._init_policy_categories()

    def _init_policy_categories(self)-> None:
        from .policy_categories import POLICY_CATEGORIES
        self.policy_categories = [POLICY_CATEGORIES[id] for id in self.policy_category_ids]

stakeholders = """
- id: funders
  title: Funders
  colour: blue
  description: Ipsum Lorem
  policy_category_ids: [communication, guidelines, fiscal, regulation, service-provision]
- id: ethics
  title: Ethics Committees
  colour: blue
  description: Ipsum Lorem
  policy_category_ids: [communication, guidelines, regulation, service-provision]
- id: institutions
  title: Institutions
  colour: blue
  description: Includes Universities, research organisations, and professional societies.
  policy_category_ids: [communication, guidelines, regulation, service-provision]
- id: publishers
  title: Publishers
  colour: blue
  description: Ipsum Lorem
  policy_category_ids: [communication, guidelines, regulation, environmental-planning, service-provision]
- id: equator
  title: EQUATOR Network
  colour: blue
  description: Ipsum Lorem
  policy_category_ids: [communication, guidelines, environmental-planning, service-provision]
- id: developers
  title: Guideline Developers
  colour: blue
  description: Ipsum Lorem
  policy_category_ids: [communication, guidelines, environmental-planning, service-provision]
"""

for stakeholder in yaml.safe_load(stakeholders):
    STAKEHOLDERS.add(Stakeholder(**stakeholder))

for stakeholder in STAKEHOLDERS:
    stakeholder.init()
  
