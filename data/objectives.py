from graphlib import TopologicalSorter
import yaml

from .bases import InstanceCollection
from .drivers import Driver
from dataclasses import dataclass

OBJECTIVES = InstanceCollection('id')

@dataclass
class Objective(Driver):
    pass

objectives = """
- id: first-understandings
  title: What do authors understand within 5 seconds?
  colour: blue
  description: Having seen the EQUATOR home page for 5 seconds, what do novice authors understand RGs to be? What benefits do they expect? And when can they be used?
  iv_changes: value-statement
  methods: five-second-test
- id: first-feelings
  title: How do authors feel after 5 seconds?
  colour: blue
  description: How does the EQUATOR home page's design and language make authors feel after 5 seconds?
  iv_changes: persuade
  methods: five-second-test
- id: search-button
  title: How easily can authors find the search button?
  colour: blue
  description: How quickly can authors find the search button?
  iv_changes: findability
  methods: time to click
- id: usable-format-checklist
  title: What would make checklists easier to use?
  colour: blue
  description: What would make checklists (in DOCX format) easier to use?
  iv_changes: usable-resources
  methods: interview-2
- id: usable-format-guidance
  title: What would make the guidance page easier to use?
  colour: blue
  description: What would make the guidance page (displayed online) easier to use?
  iv_changes: usable-resources
  methods: interview-2
- 
"""
# accessible
# citation
# easy-understand (glossary, descriptive names)
# :create-spaces
# early-acquisition
# persuade
# findable-resources
# findability (search, organisation, SEO)
# information-architecture 
# ::create-rewards
# :design-agnostic
# ?create-tools
# evidence-benefits (testimonials)
# :feedback-channels
# :item-content
# :rg-introductions
# :support




for objective in yaml.safe_load(objectives):
    OBJECTIVES.add(Objective(**objective))