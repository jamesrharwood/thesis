import os
from collections import defaultdict

import yaml
import texttable

COLS = ['**METHOD**', '**INTERVENTION COMPONENTS** (defined in previous chapter)']
COL_RANGE = range(len(COLS))
WIDTHS = [10, 90]
ALIGNMENTS = ['l' for _ in COL_RANGE]
DIR = os.getcwd()
FP = os.path.join(DIR, 'chapters', '9_defining_content', 'data', 'planning_table.yaml')
OUTPUT = os.path.join(DIR, 'chapters', '10_pilot', 'data', '__methods_table.md')


with open(FP, 'r') as f:
    data = yaml.safe_load(f)
components = []
for key_behaviour in data.values():
    for barrier in key_behaviour.values():
        ingredients = barrier['ingredients']
        for ingredient_name in ingredients.keys():
            ingredient = ingredients[ingredient_name]
            ingredient.update({'name': ingredient_name})
            components.append(ingredient)

for comp in components:
    if 'done' not in comp.keys():
        raise Exception(comp)

components = [comp for comp in components if comp.get('duplicate', False) is False]
components = [comp for comp in components if comp['done'] is True]

components_by_method = defaultdict(list)
for comp in components:
    methods_string = comp['evaluation_methods'] or "not explored"
    methods = methods_string.split(',')
    methods = [method.strip() for method in methods]
    for method in methods:
        components_by_method[method].append(comp)

method_names = {
    '5 second test': '5 Second Test',
    'think aloud': 'Think Aloud',
    'interview': 'Interview',
    'plus minus': '+/- test',
    'writing evaluation': 'Writing Evaluation',
    'not explored': 'Not Explored',
}

for key in components_by_method.keys():
    assert key in method_names, f"{key} not valid method"

table = texttable.Texttable()
table.header(COLS)
table.set_cols_width(WIDTHS)
table.set_header_align(ALIGNMENTS)
for method in method_names.keys():
    components = components_by_method[method]
    component_names = [comp['name'] for comp in components] # type: ignore
    NAMES = ",\n* ".join(component_names) # type: ignore
    NAMES = "\n* " + NAMES + "\n"
    table.add_row([method_names[method], NAMES])

text = f"""{table.draw()}

: Methods used and the intervention components they explore. Intervention components are defined in chapter {{{{< var chapters.defining-content >}}}} {{#tbl-methods-for-components}}
"""
text = text.replace("+=", "+:") # type: ignore #needed because text table doesn't specify aligntment with colons

with open(OUTPUT, 'w') as file_:
    file_.write(text)
