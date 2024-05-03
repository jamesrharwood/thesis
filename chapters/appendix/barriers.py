"Creates barriers appendix"

import os
from data.create_table import create_barriers_text

TEXT = create_barriers_text()

DIR = os.getcwd()
DIR = os.path.join(DIR, 'chapters', 'appendix', 'barriers.md')
# print('Not creating barriers.py')
with open(DIR, 'w', encoding='utf-8') as file_:
    file_.write(TEXT)
