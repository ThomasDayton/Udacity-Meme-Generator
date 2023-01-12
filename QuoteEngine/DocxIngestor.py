'''An implementation of the abstract IngestorInterface that parses .docx files.'''
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxInquestor(IngestorInterface):
    '''An implementation of the IngestorInterface that parses .docx files.'''
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''
        Parses the .docx file that "path" points to.
        Throws an error if "path" points to a file without a .docx extension.

        Arguments:
        path: A string that points to the path of the file to parse
        '''
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
        
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        
        return quotes