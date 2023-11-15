from locators.book_locators import BookLocators
from bs4 import BeautifulSoup
import re
class BookParser:
    ''' A class to take in HTML page (or part of it), and find properties of an item in it.'''

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £ {self.price}, ({self.rating} stars)>'
    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name
    
    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    # find_item_name_link() : A Light in the Attic
    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        price = float(matcher.group(1))
        # print(matcher.group(0)) string value £51.77
        return price # float value 51.77
    #find_price_item()
    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class'] # ['star-rating', 'Three']
        rating_classes = [r for r in classes if r!= 'star-rating']
        # or you can use rating_classes = filter(lambda x: x!='start-rating', classes)
        rating_number = BookParser.RATINGS.get(rating_classes[0]) # None if not found
        return rating_number