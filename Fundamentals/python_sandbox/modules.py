# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from datetime import date 

import time

#import file from location 
import validator 

#today = datetime.date.today() 

today = date.today() 
print(today)

timestamp = time.time()
print(timestamp)

email = 'abcdef@gmail.com'

if validator.validate_email(email):
  print('Valid')
else:
  print('Not valid')