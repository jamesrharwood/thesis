"Creates ideas appendix"

import os
from collections import defaultdict
from data.create_table import create_recommendations_text
from data import STAGES, CHANGES_BY_STAGE

TEXT = ""

changes_by_stage = defaultdict(list)
for change in CHANGES_BY_STAGE:
    changes_by_stage[change.stage].append(change)

for stage in changes_by_stage:
    TEXT += (f"## {STAGES[stage]}\n\n\n\n")
    TEXT += create_recommendations_text(changes_by_stage[stage])

DIR = os.getcwd()
DIR = os.path.join(DIR, 'chapters', 'appendix', 'ideas.md')
with open(DIR, 'w', encoding='utf-8') as file_:
    file_.write(TEXT)

