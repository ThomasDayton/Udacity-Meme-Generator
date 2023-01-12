'''A main Ingestor Class that encapsulates all the Ingestor classes for supported filetypes.'''
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TxtIngestor import TxtIngestor
from .CsvIngestor import CsvIngestor
from .DocxIngestor import DocxInquestor
from .PdfIngestor import PdfIngestor

class Ingestor(IngestorInterface):
    '''A main Ingestor Class that encapsulates all the Ingestor classes for supported filetypes.'''
    ingestors = [TxtIngestor, CsvIngestor, DocxInquestor, PdfIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''
        Checks which supported Ingestor class can parse the file "path" points to,
        then runs that Ingestor's "parse" method..

        Arguments:
        path: A string that points to the path of the file to parse
        '''
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)