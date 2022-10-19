import yaml

from .bases import InstanceCollection
from .drivers import Driver
from dataclasses import dataclass

POLICY_CATEGORIES = InstanceCollection('id')

@dataclass(repr=False)
class PolicyCategory(Driver):
    pass

categories = """
- id: communication
  title: Communication
  colour: blue
  description: Ipsum Lorem
- id: guidelines
  title: Guidelines
  colour: blue
  description: Ipsum Lorem
- id: fiscal
  title: Fiscal
  colour: blue
  description: Ipsum Lorem
- id: regulation
  title: Regulation
  colour: blue
  description: Ipsum Lorem
- id: legislation
  title: Legislation
  colour: blue
  description: Ipsum Lorem
- id: environmental-planning
  title: Environmental/social planning
  colour: blue
  description: Ipsum Lorem
- id: service-provision
  title: Service Provision
  colour: blue
  description: Ipsum Lorem
"""

for category in yaml.safe_load(categories):
    POLICY_CATEGORIES.add(PolicyCategory(**category))