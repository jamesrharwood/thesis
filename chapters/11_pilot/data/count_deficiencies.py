import os
import re

deficiency_demarcation = "\n\*\*"
deficiency_regex = re.compile(deficiency_demarcation)

DIR = os.path.dirname(__file__)
FILES = [
    '_clarify_tasks.qmd',
    '_describe_benefits.qmd',
    '_describe_rgs.qmd',
    '_design_benefits.qmd',
    '_design_trust.qmd',
    '_examples.qmd',
    '_results_data.qmd',
]

def count_regex_within_files(regex):
    "counts regex occurrences within data files"
    count = 0
    for filename in FILES:
        path = os.path.join(DIR, filename)
        with open(path, 'r', encoding="utf-8") as file_:
            text = file_.read()
            matches = regex.findall(text)
            count += len(matches)
    return count

def count_deficiencies():
    "counts deficiencies within data folder"
    return count_regex_within_files(deficiency_regex)