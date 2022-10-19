from .BCW_concepts import DRIVERS
from .BCW_concepts.models import InstanceCollection

import logging

class Barrier:
    __instances = InstanceCollection('id')

    def __init__(self, content:str, id: str, title: str, driver: str, relations: list=[]) -> None:
        self.content = content
        self.id = id
        self.title = title
        self.driver = DRIVERS[driver]
        self._relations = relations
        self.relations = set()
        self.__instances.add(self)

    @classmethod
    def from_markdown(cls, markdown):
        try:
            return cls(markdown.content, **markdown.metadata)
        except TypeError as e:
            logging.warning(f'Missing metadata for Markdown: {markdown}')
            raise e
    def add_relation(self, relation):
        self.relations.add(relation)

    def init_related(self) -> None:
        for id in self._relations:
            try:
                other = self.__instances[id]
                self.add_relation(other)
                other.add_relation(self)
            except KeyError:
                logging.warning(f'{id} is not a valid id for {self}')

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.id}>"

