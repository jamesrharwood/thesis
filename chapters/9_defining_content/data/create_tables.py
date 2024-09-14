"create smaller tables of intervention components"

import os
import yaml
import texttable

COLS = ['**INTERVENTION COMPONENT**', '**INTERVENTION FUNCTION**', '**BCT**']
WIDTHS = [50, 25, 25]
ALIGNMENTS =['l' for col in COLS]

DIR = os.getcwd()
DIR = os.path.join(DIR, 'chapters', '9_defining_content', 'data')
FP = os.path.join(DIR, 'planning_table.yaml')
DIR_TABLES = os.path.join(DIR, 'tables')

with open(FP, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

components = {}
for key_behaviour in data.values():
    for barrier in key_behaviour.values():
        ingredients = barrier['ingredients']
        for ingredient_name in ingredients.keys():
            ingredient = ingredients[ingredient_name]
            ingredient.update({'name': ingredient_name})
            if ingredient['id'] not in components.keys():
                components.update({ingredient['id']: ingredient})

def create_sub_table(filename: str, ids_string: str, ids_duplicate_string=None):
    OUTPUT_FILENAME = os.path.join(DIR_TABLES, filename)
    table = texttable.Texttable()
    table.header(COLS)
    table.set_cols_width(WIDTHS)
    table.set_header_align(ALIGNMENTS)
    ids = ids_string.strip().splitlines()
    for id_ in ids:
        row = create_row(id_)
        table.add_row(row)
    if ids_duplicate_string:
        ids = ids_duplicate_string.strip().splitlines()
        for id_ in ids:
            row = create_row(id_)
            row[0] = f"_{row[0]}_"
            table.add_row(row)
    with open(OUTPUT_FILENAME, 'w') as file_:
        file_.write(table.draw())  # type: ignore

def create_row(id_):
    component = components[id_]
    name = component['name']
    if not component['done']:
        name += "*"
    row = [component['name'], component['IF'], component['BCT']]
    return row



## Site organisation and search

ORGANISATION = """
centralised-hosting
open-access

search-function
seo

link-related-rgs
link-resources

decision-tools
rg-collections
embed-related-rgs
"""

create_sub_table( 'organisation.md', ORGANISATION)

## Throughout 

THROUGHOUT = """
address-authors
explain-author-responsibility
clarify-tasks
prompts-to-use-early
seo
tools-for-early-use
design-benefits
design-trust
remove-aversive-design
remove-patronizing-language
"""

create_sub_table('throughout.md', THROUGHOUT)

## Home page

HOME = """
describe-what-rgs-are
describe-when-to-use
writing-education
describe-benefits
why-complete-reporting-is-important
testimonials-nervous
evidence-benefits
testimonials-who-benefit
"""

create_sub_table('home.md', HOME)

## Introduction to RG

INTRO = """
describe-development
describe-scope
if-then-rules
no-better-rg
instruct-to-cite
doi
translations
ready-to-use
checklists
tools-for-items
tools-for-checking
tools-for-peer-reviewers
tools-for-early-use
time-to-read
time-to-apply
reassure-just-guidelines
explain-when-structure-not-prescribed
"""

INTRO_DUPLICATES = """
describe-when-to-use
describe-what-rgs-are
clarify-tasks
tools-for-early-use
link-related-rgs
link-resources
"""

create_sub_table('rg_intro.md', INTRO, INTRO_DUPLICATES)

## RG content

RG_CONTENT = """
structure
shorten
design-agnostic
provide-design-advice-separately
plain-language
define-terms
consistent-terms
digestible-structure
why-item-is-important
item-link-to-how-to-do
item-what-to-describe
examples
discussion-spaces
item-what-to-describe-when-not-done
reassure-of-limitations
examples-imperfect
location-alternatives
examples-concise-reporting
encourage-explanation
"""

RG_CONTENT_DUPLICATES = """
writing-education
describe-benefits
testimonials-who-benefit
testimonial-nervous
evidence-benefits
"""

create_sub_table('rg_content.md', RG_CONTENT, RG_CONTENT_DUPLICATES)

## FAQ 

FAQ = """
advice-when-asked-to-remove
"""

FAQ_DUP = """
describe-development
"""

create_sub_table('faq.md', FAQ, FAQ_DUP)
