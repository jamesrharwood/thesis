import os
import logging

from yaml.parser import ParserError
from typing import Type

import frontmatter
from .bases import DataclassBase

DELIM = '\n---'
SPAN = 2

def filename_to_objs(filename: str, cls: Type[DataclassBase])-> list:
    filepath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        filename
    )
    with open(filepath, 'r') as file_:
        text = file_.read()
    posts = load_multi_markdown(text)
    return [cls(content=p.content, **p.metadata) for p in posts]  # type: ignore

def load_multi_markdown(text: str)-> list:
    items = text.split(DELIM)
    items = [item for item in items if item]
    items = zip(items[::2], items[1::2])
    items = [DELIM+DELIM.join(strings) for strings in items]
    items = [load_frontmatter(item) for item in items]
    return items

def load_frontmatter(text: str)-> frontmatter.Post:
    try: 
        return frontmatter.loads(text)
    except ParserError as e:
        logging.warn("ParserError on this text:")
        print (text)
        raise e


