import os
import re

import texttable

DIR = os.getcwd()
INPUT = os.path.join(DIR, 'chapters', '11_pilot', 'data', '_results_data.qmd')
OUTPUT = os.path.join(DIR, 'chapters', '11_pilot', 'data', '__results_table.md')
SEPARATOR = re.compile(r'\n+##\s')


with open(INPUT, 'r') as file_:
    body = file_.read()
body = "\n"+body

COLS = ["Intervention component and their relevant features and barriers", "Deficiencies"]
WIDTHS = [200, 400]

table = texttable.Texttable()
table.header(COLS)
table.set_cols_width(WIDTHS)
table.set_cols_align(["l", "l"])

ICs = SEPARATOR.split(body)
for IC in ICs:
    if not IC:
        continue
    ic_id, text = IC.split('\n\n', 1)
    title = "{{< var intervention-components." + ic_id + ".title >}}"
    description = "_Features: {{< var intervention-components." + ic_id + ".description >}}_"
    barriers = "_Barriers addressed: {{< var intervention-components." + ic_id + ".barriers >}}_"
    left_col = "\n\n".join([title, description, barriers])
    row = [left_col, text]
    table.add_row(row)

table_string = "::: {.landscape .column-body-right}\n\n"
table_string += table.draw() # type: ignore
table_string += "\n\n: Intervention components, relevant website features, the barriers they address, and deficiencies identified with supportive quotes. {#tbl-deficiencies-by-component}" #type: ignore
table_string += "\n\n:::"

with open(OUTPUT, 'w') as outfile:
    outfile.write(table_string)