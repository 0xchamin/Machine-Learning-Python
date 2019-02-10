# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip modules
import camelcase

# Custom modules
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

camel = camelcase.CamelCase()
text = 'hello there world'

email = 'test@test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Not an email')