from datetime import datetime
print(datetime.now()) # my time

from datetime import datetime, timezone
print(datetime.now(timezone.utc)) # utc timings

import re

email = 'ananya.arya@google.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches) # ['ananya', 'arya', 'google', 'com']

parts = email.split('@')
name = parts[0]
domain = parts[1]
print(name)
name_split = name.split('.')
first_name = name_split[0]
last_name = name_split[1]
print(first_name)
print(last_name)
print(domain)