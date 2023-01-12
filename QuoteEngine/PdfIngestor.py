'''An implementation of the abstract IngestorInterface that parses .pdf files.'''
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PdfIngestor(IngestorInterface):
    '''An implementation of the IngestorInterface that parses .pdf files.'''
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''
        Parses the .pdf file that "path" points to.
        Throws an error if "path" points to a file without a .pdf extension.

        Arguments:
        path: A string that points to the path of the file to parse
        '''
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
        
        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        if not os.path.isdir(tmp.split('/')[1]):
            os.makedirs(tmp.split('/')[1])
        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        quotes = []
        with open(tmp, "r") as file_ref:
            for line in file_ref.readlines():
                line.strip('\n\r').strip()
                if len(line) > 3:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        
        os.remove(tmp)
        return quotes