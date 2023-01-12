'''An implementation of the abstract IngestorInterface that parses .txt files.'''
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TxtIngestor(IngestorInterface):
    '''An implementation of the IngestorInterface that parses .txt files.'''
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''
        Parses the .txt file that "path" points to.
        Throws an error if "path" points to a file without a .txt extension.

        Arguments:
        path: A string that points to the path of the file to parse
        '''
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
        
        quotes = []

        with open(path, 'r') as file:
            for line in file.readlines():
                line.strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        
        return quotes