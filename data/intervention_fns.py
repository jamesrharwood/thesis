import yaml

from .bases import InstanceCollection
from .drivers import Driver
from dataclasses import dataclass

i_fns = """
- id: education
  title: Education
  colour: blue
  description: Increasing knowledge or understanding
- id: training
  title: Training
  colour: blue
  description: Imparting skills
- id: modelling
  title: Modelling
  colour: blue
  description: Provide an example for people to aspire to or imitate
- id: persuasion
  title: Persuasion
  colour: blue
  description: Using communication to induce positive or negative feelings or stimulate action
- id: coercion
  title: Coercion
  colour: blue
  description: Creating an expectation of punishment or cost
- id: restriction
  title: Restriction
  colour: blue
  description: Using rules to reduce the opportunity to engage in the target behaviour (or to increase the target behaviour by reducing the opportunity to engage in competing behaviours)
- id: incentivization
  title: Incentivization
  colour: blue
  description: Creating an expectation of reward
- id: environmental-restructuring
  title: Environmental Restructuring
  colour: blue
  description: Changing the physical or social context
- id: enablement
  title: Enablement
  colour: blue
  description: Increasing means/reducing barriers to increase capability (beyond education and training) or opportunity (beyond environmental restructuring)
"""

INTERVENTION_FNS = InstanceCollection('id')

@dataclass
class InterventionFun(Driver):
    pass

for i_fn in yaml.safe_load(i_fns):
    INTERVENTION_FNS.add(InterventionFun(**i_fn))