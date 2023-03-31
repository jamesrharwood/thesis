import yaml

from data import BARRIERS, CHANGES, STAKEHOLDERS, STAGES

participants = 16 #TODO
focus_groups = 7 #TODO
guideline_developers = 11 #TODO
publishers = 3 #TODO
academics = 2 #TODO

sub_item_count = 0
jh_ideas_count = 0
jh_ideas_before = 'TODO'

for change in CHANGES:
    sub_item_count += change.idea_count
    jh_ideas_count += change.content.count('^JH^')

counts = dict(
    barriers = len(BARRIERS.values()),
    stakeholders = len(STAKEHOLDERS.values()),
    changes = len(CHANGES.values()),
    sub_items = sub_item_count,
    sub_items_pre_jh = sub_item_count - jh_ideas_count,
    jh_ideas = jh_ideas_count,
    jh_ideas_before = jh_ideas_before,
    EQUATOR_ideas = 'TODO',
    participants = participants,
    focus_groups = focus_groups,
    guideline_developers = guideline_developers, 
    academics = academics, 
    publishers = publishers,
)


stages_strs = list(STAGES.values())
stages_strs = [s.lower() for s in stages_strs]
stages_str = ', '.join(stages_strs[:-1]) + ', or ' + stages_strs[-1]

stakeholders_strs = [s.title.lower() for s in STAKEHOLDERS]
stakeholders_str = ', '.join(stakeholders_strs[:-1]) + ', and ' + stakeholders_strs[-1]

descriptions = dict(
    stages = stages_str,
    stakeholders = stakeholders_str,
)

filename = "_variables.yml"

changes = {c.id: c.title for c in CHANGES}
changes_section_titles = {c.id: c.title.lower().replace(' ', '-') for c in CHANGES}
barriers = {b.id: b.title for b in BARRIERS}
barrier_sections = {b.id: b.title.lower().replace(' ', '-') for b in BARRIERS}
with open(filename, 'r+') as file_:
    variables = yaml.safe_load(file_)
    file_.seek(0)
    if variables is None:
        variables = {}
    if not 'counts' in variables:
        variables.update({'counts': {}})
    variables['counts'].update(counts)
    variables.update({'descriptions': descriptions})
    stages = STAGES
    variables.update({'stages': stages})
    variables.update({'IFs':  changes})
    variables.update({'IFSecs': changes_section_titles})
    variables.update({'BARRIERS': barriers})
    variables.update({'BARRIER_SECTIONS': barrier_sections})
    yaml.dump(variables, file_, width=1000)
    file_.truncate()
