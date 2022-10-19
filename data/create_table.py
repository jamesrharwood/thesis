import texttable

from data import BARRIERS, CHANGES, CHANGES_BY_STAGE
from .iv_changes import Change

SPACE = "&ensp;"
H8 = "#"*8
H9 = "#"*9

def create_recommendations_table():
    tb = texttable.Texttable()
    tb.header(["Recommendation", "Barriers"])
    tb.set_cols_width([50, 50])
    for c in CHANGES:
        text = f"#### {c.title}{{#sec-{c.id}}}"
        text += f"\n\n{c.content}"
        IFs = join_items(c.intervention_fns, create_abbr)
        text += f"\n\n<small>Intervention functions:{SPACE}{IFs}</small>"
        barriers = "\n\n"+join_items(c.barriers, create_link, '\n\n')
        tb.add_row([text, barriers])
    return tb

def create_barriers_table():
    tb = texttable.Texttable()
    tb.header(["Barrier", "Recommendations"])
    # tb.set_cols_width([80, 20])
    for b in BARRIERS:
        text = f"#### {b.title}{{#sec-{b.id}}}"
        text += f"\n\n{b.content}"
        DRIVER = join_items([b.driver], create_abbr)
        text += f"\n\n<small>Behavioural Driver:{SPACE}{DRIVER}</small>"
        recommendations = "\n\n"+join_items(b.changes, create_link, '\n\n')
        tb.add_row([text, recommendations])
    return tb

def join_items(items, fn, delim=f";{SPACE}"):
    strings = [fn(i) for i in items]
    return delim.join(strings)

def create_link(item):
    return f"[{item.title}](#sec-{item.id})"

def create_abbr(item):
    return f"<abbr title='{item.description}'>{item.title}</abbr>"

def create_text(iterable, relationships_str, relationships_attr, bcw_concept_name, bcw_concept_attr):
    s = ""
    for idx, c in enumerate(iterable):
        s += f"## {idx+1}: " + c.title + "{#sec-" + c.id + "}\n\n"
        s += c.content + "\n\n"
        concepts = getattr(c, bcw_concept_attr)
        concepts = [concepts] if type(concepts) is not list else concepts
        concepts = [c.title for c in concepts]
        s += f"{H8} {bcw_concept_name}: {', '.join(concepts)}\n\n"
        s += f"{H8} " + f"{relationships_str}:\n\n"
        for b in getattr(c, relationships_attr):
            s += f"{H9} [{b.title}](#sec-{b.id})\n"
            s += "\n"
        s += "\n\n"
    return s

def create_barriers_text():
    return create_text(BARRIERS, 'Recommendations', 'changes', 'Behavioural Driver', 'driver')

def create_recommendations_text():
    # return create_text(CHANGES_BY_STAGE, 'Barriers addressed', 'barriers', 'Intervention Functions', 'intervention_fns')
    return join_lines(
        *[join_lines(
            create_title(idx, change),
            change.content,
            create_subtitle('Intervention Functions') + create_inline_list(change.intervention_fns),
            # create_subtitle('Stakeholders') + create_inline_list(change.stakeholders),
            create_subtitle('Barriers'),
            create_linked_list(change.barriers),
        ) for idx, change in enumerate(CHANGES_BY_STAGE)]
    )

def create_title(idx, item):
    return f"## {idx+1}: " + item.title + "{#sec-" + item.id + "}"

def create_subtitle(text):
    return f"{H8} {text}: "

def create_inline_list(iterable):
    return ', '.join([i.title for i in iterable])

def create_linked_list(iterable):
    lines = [f"{H9} [{i.title}](#sec-{i.id})" for i in iterable]
    return '\n'.join(lines)



def join_lines(*args):
    return '\n\n'.join(args)
