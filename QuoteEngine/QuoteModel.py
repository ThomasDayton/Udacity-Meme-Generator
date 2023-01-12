'''A module containing a simple class that stores the body and author of a quote.'''

class QuoteModel():
    '''Simple class that encapsulates the body and author of a given quote.'''
    def __init__(self, body, author):
        '''
        Create a QuoteModel Object.

        Arguments:
        quote_body: The body of the quote.
        quote_author: The author of the quote.
        '''
        self.body = body.replace('"', '')
        self.author = author
    
    def print(self):
        '''
        Override the print method to return a string representation of the quote,
        formatted as "[quote_body]" - [quote_author].
        '''
        return f'"{self.body}" - {self.author}'