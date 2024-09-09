import os
import texttable
from collections import defaultdict
from data import STAGES, CHANGES_BY_STAGE

DIR = os.getcwd()
FP = os.path.join(DIR, 'chapters', '8_focus_groups', '_table_results.qmd')

table = texttable.Texttable()
table.set_cols_align(['l', 'l'])
table.set_header_align(['l', 'l'])
table.set_max_width(0)
table.header(('Ideas', 'Influences'))

changes_by_stage = defaultdict(list)
for change in CHANGES_BY_STAGE:
    changes_by_stage[change.stage].append(change)

rows = []
for stage, ideas in changes_by_stage.items():
    text = f"**{STAGES[stage]}**"
    rows.append([text, ''])
    for idea in ideas:
        barriers = [b.title for b in idea.barriers]
        barriers = '\n\n'.join(barriers)
        rows.append([idea.title, barriers])
    
table.add_rows(rows, header=False)
CAPTION = "\n\n\n\n: Broad ideas and the influences "\
    "they target, categorised by when they should "\
    "be considered.  Influences were derived and consolidated in previous chapters, and are reported fully in Appendix {{< var appendix.barriers >}}) {#tbl-focus-groups-results}"

with open(FP, 'w') as file_:
    text = table.draw()
    text = text.replace("+=", "+:") # type: ignore #needed because text table doesn't specify aligntment with colons
    text += CAPTION # type: ignore
    file_.write(text) # type: ignore
