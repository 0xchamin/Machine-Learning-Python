# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
# numbers = [1,2,3,4,5]
# Using a constructor
numbers = list((1,2,3,4,5))
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get value
print(fruits[1])

# Get len
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove from position
fruits.pop(3)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)