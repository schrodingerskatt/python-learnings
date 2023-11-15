from bs4 import BeautifulSoup


SIMPLE_HTML = '''
<head></head>
<body>
<h1> This is title </h1>
<p class= "subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p> Here's another p without a class </p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
<body>
<html>'''

# parsing
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')
parser = simple_soup.find('h1') # <h1> This is title </h1>
print(parser.string) # will give only contents : This is title

def find_list():
    li_parser = simple_soup.find_all('li')
    print(li_parser) # [<li>Rolf</li>, <li>Charlie</li>, <li>Jen</li>, <li>Jose</li>]
    list_contents = [e.string for e in li_parser]
    print(list_contents) # ['Rolf', 'Charlie', 'Jen', 'Jose']

find_list()

# to find p tag with class subtitle
def find_subtitle():
    paragraph = simple_soup.find('p',{'class':'subtitle'})
    print(paragraph.string)

find_subtitle() # Lorem ipsum dolor sit amet. Consectetur edipiscim elit.

# only <p>

def find_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraphs = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    # p.attrs.get('class') return none if it can't find the class, since 'none' is not iterable use p.attrs.get('class', [])
    # it will return [] if it encounters none
    # or we can use p.attrs['class']
    print(other_paragraphs[0].string)

find_paragraph()