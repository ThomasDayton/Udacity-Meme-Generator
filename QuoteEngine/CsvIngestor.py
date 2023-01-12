'''An implementation of the abstract IngestorInterface that parses .csv files.'''
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CsvIngestor(IngestorInterface):
    '''An implementation of the IngestorInterface that parses .csv files.'''
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''
        Parses the .csv file that "path" points to.
        Throws an error if "path" points to a file without a .csv extension.

        Arguments:
        path: A string that points to the path of the file to parse
        '''
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
        
        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        
        return quotes
        