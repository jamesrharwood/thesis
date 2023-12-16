import yaml, os, importlib

from collections import defaultdict

import frontmatter 

from data import BARRIERS, CHANGES, STAKEHOLDERS, STAGES

count_deficiencies = importlib.import_module("chapters.11_pilot.data.count_deficiencies")
participant_ids = importlib.import_module("chapters.11_pilot.data.participant_ids")


participants = 16 #TODO
focus_groups = 7 #TODO
guideline_developers = 11 #TODO
publishers = 3 #TODO
academics = 2 #TODO

sub_idea_count = 0
jh_ideas_count = 0

for change in CHANGES:
    sub_idea_count += change.idea_count
    jh_ideas_count += change.content.count('^JH^')

## Intervention components count
DIR = os.getcwd()
FP = os.path.join(DIR, 'chapters', '9_defining_content', 'planning_table.yaml')
ICs_TOTAL = 0
ICs_INCLUDED = 0
ICs_UNIQUE = 0
ICs_INCLUDED_UNIQUE = 0
IC_BARRIERS = set()
IC_INTERVENTION_FUNCTIONS = set()
IC_BCTs = set()
ICs = defaultdict(lambda: {'title':None, 'description': None, 'barriers':''})

with open(FP, 'r') as f:
    data = yaml.safe_load(f)

for key_behaviour in data.keys():
    for barrier in data[key_behaviour].keys():
        IC_BARRIERS.add(barrier)
        for ingredient_name, ingredient in data[key_behaviour][barrier]['ingredients'].items():
            if type(ingredient) is not dict:
                print (data[key_behaviour][barrier])
            ICs_TOTAL += 1
            is_unique = not(ingredient.get('duplicate', False))
            if is_unique:
                ICs_UNIQUE += 1
                IC_INTERVENTION_FUNCTIONS.add(ingredient['IF'])
                for bct in ingredient['BCT'].split(','):
                    IC_BCTs.add(bct.strip()) #TODO some components have multiple BCTs listed. Either reduce to only one, or split on comma
                ICs[ingredient['id']]['title'] = ingredient_name
                ICs[ingredient['id']]['description'] = ingredient['now']
            if ingredient['done']:
                ICs_INCLUDED += 1
                if is_unique:
                    ICs_INCLUDED_UNIQUE += 1
            barrier_title = BARRIERS[barrier].title
            if barrier_title not in ICs[ingredient['id']]['barriers']:
                barriers = ICs[ingredient['id']]['barriers']
                if barriers:
                    barriers += "; "
                barriers += barrier_title
                ICs[ingredient['id']]['barriers'] = barriers
ICs = dict(ICs)

INTERVENTION_COMPONENTS = {
    'total': ICs_TOTAL,
    'unique': ICs_UNIQUE,
    'included': ICs_INCLUDED,
    'included_unique': ICs_INCLUDED_UNIQUE,
    'not_included_unique': ICs_UNIQUE - ICs_INCLUDED_UNIQUE,
}
IC_BARRIERS = set([b.lower() for b in IC_BARRIERS if b])
IC_INTERVENTION_FUNCTIONS = set([i.lower() for i in IC_INTERVENTION_FUNCTIONS if i])
IC_BCTs = set(bct.lower() for bct in IC_BCTs if bct)

counts = dict(
    barriers = len(BARRIERS.values()),
    stakeholders = len(STAKEHOLDERS.values()),
    changes = len(CHANGES.values()),
    sub_ideas = sub_idea_count,
    sub_ideas_pre_jh = sub_idea_count - jh_ideas_count,
    jh_ideas = jh_ideas_count,
    EQUATOR_ideas = 'TODO', #TODO
    participants = participants,
    focus_groups = focus_groups,
    guideline_developers = guideline_developers,
    academics = academics,
    publishers = publishers,
    redesign = {
        'intervention-components': INTERVENTION_COMPONENTS,
        'barriers-targeted': len(IC_BARRIERS),
        'intervention-functions-used': len(IC_INTERVENTION_FUNCTIONS),
        'bcts-used': len(IC_BCTs),
    },
    pilot = {
        'deficiencies': count_deficiencies.count_deficiencies(),
    },
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

with open('metadata/chapters.txt', 'r') as file_:
    chapters = file_.readlines()
    chapters = {
        chapter.strip(): idx+1 for idx, chapter in enumerate(chapters)
    }

FILEPATHS=[
    "chapters/1_introduction/index.qmd",
    "chapters/2_reflexivity/index.qmd",
    "chapters/3_synthesis/index.qmd",
    "chapters/4_survey_content/index.qmd",
    "chapters/5_website_audit/index.qmd",
    "chapters/6_bcw/index.qmd",
    "chapters/7_workshops/index.qmd",
    "chapters/8_focus_groups/index.qmd",
    "chapters/9_defining_content/index.qmd",
    "chapters/10_redesign/index.qmd",
    "chapters/11_pilot/index.qmd",
    #"output/chapters/discussion"
]

titles = {}
for fp in FILEPATHS:
    with open(fp, 'r') as f:
        text = f.read()
        fm = frontmatter.loads(text)
        title = fm.metadata['title']
        chapter = fp.split('/')[1].split('_', 1)[1]
        titles.update({chapter: title})

PARTICIPANT_IDS = {key: f"(value)" for key, value in participant_ids.PARTICIPANT_IDS.items()}
pilot = {'participants': PARTICIPANT_IDS}

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
    variables.update({'chapters': chapters})
    variables.update({'titles': titles})
    variables.update({'intervention-components': ICs})
    variables.update({'pilot': pilot})
    variables.update()
    yaml.dump(variables, file_, width=1000)
    file_.truncate()
