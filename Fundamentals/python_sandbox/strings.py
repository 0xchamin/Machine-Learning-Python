# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


# String Formatting

name =  "Chamin"
age = 24
print('Hello '+name+' and I\'m  '+ str(age)+' years old')



#Arguments by position
print('{}, {}, {}'.format('a', 2,'c'))
print('{1}, {2}, {0}'.format('Chamin', 2,'Nalinda'))

#Arguments by name 
print("My name is {name} and I am {age} years old".format(name=name, age= 28))


#F-strings 
print(f'My name is {name} and I am {age}')

# String Methods

s = 'Hello World'
#capitalize first letter 
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())

#get length
print(len(s))

#replace 
print(s.replace('World', 'Girls'))

#count 
sub = "H"
print(s.count(sub))