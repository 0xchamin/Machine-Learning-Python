# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


def sayHello(name = 'Jerry'):
  """
  Prints Hello and then name 
  """
  print('Hello {name}'.format(name=name))

sayHello('Angel')



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1+num2 
print(getSum(3,5))

addOneToNum = lambda num: num+1
print(addOneToNum(4))

