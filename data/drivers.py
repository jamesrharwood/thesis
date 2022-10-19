import yaml

from .bases import InstanceCollection, DataclassBase
from dataclasses import dataclass

drivers = """
- id: capability
  title: Capability
  colour: blue
  description: Ipsum Lorem
- id: opportunity
  title: Opportunity
  colour: red
  description: Ipsum Lorem
- id: motivation
  title: Motivation
  colour: yellow
  description: Ipsum Lorem
"""

DRIVERS = InstanceCollection('id')

@dataclass(repr=False)
class Driver(DataclassBase):
    id: str
    title: str
    colour: str
    description: str

for driver in yaml.safe_load(drivers):
    DRIVERS.add(Driver(**driver))
