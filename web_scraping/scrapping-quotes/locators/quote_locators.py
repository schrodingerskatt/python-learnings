''' quote locators are used when we want to extract information from a single quote.
'''

class QuoteLocators:
    AUTHOR ='small.author' # <small class="author" itemprop="author">Albert Einstein</small>
    CONTENT = 'span.text' # 
    TAGS = 'div.tags a.tag'
       