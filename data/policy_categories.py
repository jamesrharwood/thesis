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
  description: Using print, electronic, telephonic or broadcast media
- id: guidelines
  title: Guidelines
  colour: blue
  description: Creating documents that recommend or mandate practice - this includes all changes to service provision
- id: fiscal
  title: Fiscal
  colour: blue
  description: Using the tax system to reduce or increase the financial cost
- id: regulation
  title: Regulation
  colour: blue
  description: Establishing rules or principles of behaviour or practice
- id: legislation
  title: Legislation
  colour: blue
  description: Making or changing laws
- id: environmental-planning
  title: Environmental/social planning
  colour: blue
  description: Designing and/or controlling the physical or social environment
- id: service-provision
  title: Service Provision
  colour: blue
  description: Delivering a service
"""

for category in yaml.safe_load(categories):
    POLICY_CATEGORIES.add(PolicyCategory(**category))