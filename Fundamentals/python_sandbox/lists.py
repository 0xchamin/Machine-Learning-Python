# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,2,3,4,5]
print(type(numbers))

fruits = ['Apple', 'Orange', 'Banana', 'Grapes', 'Papow']

mixed = ['a',1,'ab']


print(len(mixed))

#insert into specific position
fruits.insert(2, 'Strawberries')
print(fruits)

#remove from index
fruits.pop(3)
print(fruits)

#reverse
print(fruits.reverse())

#sorted
print(fruits.sort())
print(fruits.sort(reverse=True))