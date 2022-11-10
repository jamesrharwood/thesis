import yaml

from data import BARRIERS, CHANGES, STAKEHOLDERS, STAGES

sub_item_count = 0
jh_ideas_count = 0

for change in CHANGES:
    items = change.content.splitlines()
    items = [item for item in items if item]
    sub_item_count += len(items)
    jh_ideas_count += change.content.count('^JH^')

counts = dict(
    barriers = len(BARRIERS.values()),
    stakeholders = len(STAKEHOLDERS.values()),
    changes = len(CHANGES.values()),
    sub_items = sub_item_count,
    sub_items_pre_jh = sub_item_count - jh_ideas_count,
    jh_ideas = jh_ideas_count,
)


stages = list(STAGES.values())
stages = [s.lower() for s in stages]
stages = ', '.join(stages[:-1]) + ', or ' + stages[-1]

stakeholders = [s.title.lower() for s in STAKEHOLDERS]
stakeholders = ', '.join(stakeholders[:-1]) + ', and ' + stakeholders[-1]

descriptions = dict(
    stages=stages,
    stakeholders=stakeholders,
)

filename = "_variables.yml"

with open(filename, 'r+') as file_:
    variables = yaml.safe_load(file_)
    file_.seek(0)
    if variables is None:
        variables = {}
    if not 'counts' in variables:
        variables.update({'counts': {}})
    variables['counts'].update(counts)
    variables.update({'descriptions': descriptions})
    yaml.dump(variables, file_)
    file_.truncate()
