import texttable

from data import BARRIERS, CHANGES, CHANGES_BY_STAGE
from .iv_changes import Change

SPACE = "&ensp;"
H8 = "#"*8
H9 = "#"*9

LEFT_COL = """\
#### {title}{{#sec-{id}}}

{content}"""

RIGHT_COL = f"#### {SPACE}\n\n\n\n{{body}}"

CHANGES_RIGHT_COL = f"""\
{H8} Barriers addressed:

{{barriers}}



{H8} Functions:{SPACE}{{intervention_fns}}



{H8} Who:{SPACE}{{stakeholders}}
"""
CHANGES_RIGHT_COL = RIGHT_COL.format(body=CHANGES_RIGHT_COL)

BARRIERS_RIGHT_COL = f"""\
{H8} Ideas:

{{changes}}



{H8} Behavioural driver: {{driver}}
"""
BARRIERS_RIGHT_COL = RIGHT_COL.format(body=BARRIERS_RIGHT_COL)

def create_table(rows=None, row=None, header=None):
    assert rows or row
    tb = texttable.Texttable()
    tb.set_cols_align(['l', 'l'])
    tb.set_max_width(0)
    if header:
        tb.header(header)
    if rows:
        tb.add_rows(rows, header=False)
    else:
        tb.add_row(row)
    return tb

def create_recommendations_table(changes):
    rows = []
    for c in changes:
        left_col = LEFT_COL.format(
            title=c.title,
            id=c.id,
            content=c.content,
        )
        IFs = join_items(c.intervention_fns, create_abbr)
        stakeholders = join_items(c.stakeholders, create_abbr)
        barriers = f"{H9} "+join_items(c.barriers, create_link, f'\n\n{H9} ')
        right_col = CHANGES_RIGHT_COL.format(
            barriers=barriers,
            intervention_fns=IFs,
            stakeholders=stakeholders,
            )
        rows.append([left_col, right_col])
    tb = create_table(rows=rows)
    return tb

def create_barriers_table():
    rows = []
    for b in BARRIERS:
        left_col = LEFT_COL.format(title=b.title, id=b.id, content=b.content)
        driver = join_items([b.driver], create_abbr)
        changes = f"{H9} "+join_items(b.changes, create_link, f'\n\n{H9} ')
        right_col = BARRIERS_RIGHT_COL.format(changes=changes, driver=driver)
        rows.append([left_col, right_col])
    tb = create_table(rows=rows)
    return tb

def join_items(items, fn, delim=f";{SPACE}"):
    strings = [fn(i) for i in items]
    return delim.join(strings)

def create_link(item):
    return f"[{item.title}](#sec-{item.id})"

def create_abbr(item):
    return f"<abbr title='{item.description}'>{item.title}</abbr>"

def create_text(iterable, relationships_str, relationships_attr): #, bcw_concept_name, bcw_concept_attr):
    s = ""
    for idx, c in enumerate(iterable):
        s += f"## " + c.title + "{#sec-" + c.id + "}\n\n"
        s += c.content + "\n\n"
        # concepts = getattr(c, bcw_concept_attr)
        # concepts = [concepts] if type(concepts) is not list else concepts
        # concepts = [c.title for c in concepts]
        # s += f"{H8} {bcw_concept_name}: {', '.join(concepts)}\n\n"
        s += f"{H8} " + f"{relationships_str}:\n\n"
        for b in getattr(c, relationships_attr):
            s += f"{H9} [{b.title}](#sec-{b.id})\n"
            s += "\n"
        s += "\n\n"
    return s

def create_barriers_text():
    return create_text(BARRIERS, 'Ideas to address this influence', 'changes') #, 'Behavioural Driver', 'driver')

def create_recommendations_text(changes):
    # return create_text(CHANGES_BY_STAGE, 'Barriers addressed', 'barriers', 'Intervention Functions', 'intervention_fns')
    return join_lines(
        *[join_lines(
            create_title(idx, change),
            change.content,
            # create_subtitle('Intervention Functions') + create_inline_list(change.intervention_fns),
            create_subtitle('Who could do this') + create_inline_list(change.stakeholders),
            create_subtitle('Influences addressed'),
            create_linked_list(change.barriers),
            '\n\n\n\n'
        ) for idx, change in enumerate(changes)]
    )

def create_title(idx, item):
    # return f"## {idx+1}: " + item.title + "{#sec-" + item.id + "}"
    return f"## " + item.title + "{#sec-" + item.id + "}"

def create_subtitle(text):
    return f"{H8} {text}: "

def create_inline_list(iterable):
    return ', '.join([i.title for i in iterable])

def create_linked_list(iterable):
    lines = [f"{H9} [{i.title}](#sec-{i.id})" for i in iterable]
    return '\n'.join(lines)

def join_lines(*args):
    return '\n\n'.join(args)
