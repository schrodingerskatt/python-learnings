import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''
class ParsedItemLocators:
    '''
    Locators for an item in the HTML page.
    This allows us to easily see what our code will be looking at as well as change it quickly,
    if we notice it is now different.
    '''
    NAME_LINK_LOCATOR = 'article.product_pod h3 a' # CSS locator
    PRICE_LOCATOR ='article.product_pod p.price_color'
    RATING_LOCATOR ='article.product_pod p.star-rating'
class ParsedItem:
    ''' A class to take in HTML page (or part of it), and find properties of an item in it.'''

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
    @property
    def name_link(self):
        locator = ParsedItemLocators.NAME_LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        item_href = item_link.attrs['href']
        item_name = item_link.attrs['title']
        return (item_name, item_href)

    # find_item_name_link() : A Light in the Attic
    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        # print(matcher.group(0)) string value £51.77
        return(matcher.group(1)) # float value 51.77
    #find_price_item()
    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class'] # ['star-rating', 'Three']
        rating_classes = [r for r in classes if r!= 'star-rating']
        # or you can use rating_classes = filter(lambda x: x!='start-rating', classes)
        return(rating_classes[0])

    #find_item_rating()

item = ParsedItem(ITEM_HTML)
name, link = item.name_link
print(name)
print(link)
print(item.rating)
print(item.price)
'''
1. In Python, @property is a decorator that is used to define a property for a class. 
2. Properties allow you to access and set the value of an attribute using the same syntax as getting or 
   setting an attribute, while allowing you to execute code upon access or modification. 
3. This can be useful for creating more controlled and flexible interfaces for your classes.
'''