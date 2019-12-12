# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#core modules
import datetime
import time 

today = datetime.date.today()
print(f'today {today}')

timestamp = time.time()
print(f'now {timestamp}')

#pip modules
from camelcase import CamelCase
c = CamelCase()
print(c.hump('Hello there world'))

# import custom module
import validator

email = 'test' 
if validator.validate_email(email):
    print('email is valid')
else:
    print('email is bad')
