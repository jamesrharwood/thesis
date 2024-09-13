"Creates intervention component table"

import os
import yaml

import texttable

from data import BARRIERS

TEXT = ""

SEE_ABOVE = ""

COLS = [
    'Intervention Ingredient',
    "Behaviour Change Technique",
    'Intervention Function', 
    'Before', 
    'Now', 
]
COLS = [f"**{col}**" for col in COLS]
COL_RANGE = range(len(COLS))
WIDTHS = [400, 200, 200, 400, 400]
ALIGNMENTS = ['l' for _ in COL_RANGE]
DIR = os.getcwd()
FP = os.path.join(DIR, 'chapters', '9_defining_content', 'data', 'planning_table.yaml')
with open(FP, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
table = texttable.Texttable()
table.header(COLS)
table.set_cols_width(WIDTHS)
table.set_header_align(ALIGNMENTS)
for key_behaviour, barriers in data.items():
    table.add_row([f'[**Key Behaviour: {key_behaviour}**]{{.nowrap .text-info}}', '', '', '', ''])
    for barrier, details in barriers.items():
        target = BARRIERS[barrier].driver.title
        text = f'[**Targeted barrier: {BARRIERS[barrier].title}**]{{.nowrap}}'
        text += '\n\n'
        text += f'[**Behavioural driver: {target}**]{{.nowrap}}'
        table.add_row([text, '', '', '', ''])
        ingredients = details['ingredients']
        if isinstance(ingredients, dict):
            for desc, values in ingredients.items():
                try:
                    before = f'{values["before"] or SEE_ABOVE}'
                    examples = values["before_example"]
                    if examples: 
                        before += f'\n\nExample: {examples}'
                    now = f'{values["now"] or SEE_ABOVE}'
                    examples = values["now_example"]
                    if examples: 
                        now += f'\n\nExample: {examples}'
                    BCT = values['BCT'] or SEE_ABOVE
                    done = values['done']
                    assert isinstance(done, bool)
                    if not done:
                        desc += "*"
                except Exception as e:
                    print(values)
                    raise Exception(desc) from e # type: ignore
                IF = values.get('IF', SEE_ABOVE)
                table.add_row([desc, BCT, IF, before, now])
TEXT += table.draw() # type: ignore
TEXT += "\n\n"
TEXT += ": Intervention Components Table. Intervention components labelled with the behaviour change techniques and intervention functions they employ, and grouped according to the key behaviours, barriers, and behavioural drivers that they aim to target. Where possible, examples demonstrate how components were (or were not) used originally (Before) and, how they are included within the redesigned intervention (Now). {#tbl-int-plan}"

OUT_FP = os.path.join(DIR, 'chapters', 'appendix', 'intervention_component_table.md')
with open(OUT_FP, 'w', encoding='utf-8') as file_:
    file_.write(TEXT)
