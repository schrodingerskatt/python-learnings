from locators.quote_locators import QuoteLocators

class QuoteParser:
    '''
    Given one of the specific quote divs, find out the data about 
    the quote (quote content, author, tags).
    '''

    def __init__(self, parent):
        self.parent = parent
    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'
    @property
    def content(self):
        locators = QuoteLocators.CONTENT
        return self.parent.select_one(locators).string
    @property
    def author(self):
        authors = QuoteLocators.AUTHOR
        return self.parent.select_one(authors).string
    @property
    def tags(self):
        tags = QuoteLocators.TAGS
        return self.parent.select_one(tags).string
    