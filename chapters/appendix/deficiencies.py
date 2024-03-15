"Creates appendix listing all deficiencies"

import os
import re
import texttable
import yaml

DIR = os.getcwd()
DIR = DIR[:DIR.find('thesis')+len('thesis')]
VAR_FILE = os.path.join(DIR, '_variables.yml')

with open(VAR_FILE, 'r', encoding='utf-8') as file_:
    VAR = yaml.load(file_.read(), yaml.Loader)

IN_FILE = os.path.join(DIR, 'chapters', '10_pilot', 'data', '_results_data.qmd')
OUT_FILE = os.path.join(DIR, 'chapters', 'appendix', 'deficiencies.md')

SEPARATOR = re.compile(r'\n+##\s')

with open(IN_FILE, 'r') as file_:
    body = file_.read()
body = "\n"+body

COLS = ["Intervention components, their relevant features, and barriers", "Deficiencies"]
widths = [0, 0]

table = texttable.Texttable()
table.header(COLS)
table.set_cols_align(["l", "l"])
table.set_header_align(["l", "l"])

ICs = SEPARATOR.split(body)
# for IC in ICs:
#     if not IC:
#         continue
#     ic_id, text = IC.split('\n\n', 1)
#     title = "**Intervention component: "+VAR["intervention-components"][ic_id]["title"]+"**"
#     description = f'_Relevant website features: {VAR["intervention-components"][ic_id]["description"]}_'
#     barriers = f'_Barriers addressed: {VAR["intervention-components"][ic_id]["barriers"]}_'
#     left_col = "\n\n".join([title, description, barriers])
#     row = [left_col, text]
#     table.add_row(row)
#     widths[0] = max([widths[0], len(title), len(description), len(barriers)])
#     widths[1] = max([widths[1], max([len(x) for x in text.splitlines()])])
# table.set_cols_width(widths)

# with open(OUT_FILE, 'w', encoding='utf-8') as out_file:
#     out_file.write(table.draw()) #type: ignore

H8 = "#"*8
H9 = "#"*9

text = ""

for IC in ICs:
    if not IC:
        continue
    ic_id, ic_text = IC.split('\n\n', 1)
    text += "### " + VAR["intervention-components"][ic_id]["title"]
    text += "\n\n"
    text += H8 + " Relevant website features: " +  VAR["intervention-components"][ic_id]["description"]
    text += "\n\n"
    text += H8 + " Barriers addressed: " + VAR["intervention-components"][ic_id]["barriers"]
    text += "\n\n"
    text += ic_text 
    text += "\n\n"

with open(OUT_FILE, 'w', encoding='utf-8') as out_file:
    out_file.write(text)
