'''A module containing an abstract base class for the quote ingestors.'''

from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    '''Abstract Class for the quote ingestors'''

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        '''
        Check if the Ingestor is designed for the file "path" points to.

        Arguments:
        path: A string that points to the path of the file to parse
        '''
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''
        An abstract method that will be overridden to parse the file "path" points to.
        
        Arguments:
        path: A string that points to the path of the file to parse
        '''
        pass