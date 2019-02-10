# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#simple dictionary 
person = {
  'first_name': 'Chamin',
  'last_name': 'Nalinda',
  'age': 28
}

print(person)

#using constructor 
person2 = dict(first_name='Chamin',last_name='Nalinda',age=28)
print(person2)

#accessvalue 
print(person['first_name'])
print(person.get('last_name'))

#add key 
person['phone'] = '555-555-555'
print(person)

#get keys 
print(person.keys())

#get values 
print(person.items())

#make a copy 
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)
print(person)

#remove item 
del person3['age']
print(person3)
person3.pop('phone')

# clear 
person3.clear()

print(len(person3))


# list of dicitonaries 
people = [
          {'name': 'Martha', 'age': 40},
          {'name': 'Bob', 'age': 20},
          ]

print(people)

print(people[1]['name'])
