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

soup = BeautifulSoup(ITEM_HTML, 'html.parser')

def find_item_name_link():
    locator = 'article.product_pod h3 a' # CSS locator
    item_link = soup.select_one(locator)
    item_href = item_link.attrs['href']
    print(item_href)
    item_name = item_link.attrs['title']
    print(item_name)

find_item_name_link() # A Light in the Attic

def find_price_item():
    locator = 'article.product_pod p.price_color'
    item_price = soup.select_one(locator).string
    pattern = '£([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_price)
    print(matcher.group(0)) # string value £51.77
    print(matcher.group(1)) # float value 51.77
find_price_item()

def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class'] # ['star-rating', 'Three']
    rating_classes = [r for r in classes if r!= 'star-rating']
    # or you can use rating_classes = filter(lambda x: x!='start-rating', classes)
    print(rating_classes[0])

find_item_rating()

