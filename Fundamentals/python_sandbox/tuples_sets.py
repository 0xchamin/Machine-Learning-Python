# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

fruites_tuple = ('Apple', 'Orange', 'Mango')
print(fruites_tuple)

fruites_tuple2 = tuple(('Apple', 'Orange', 'Grapes'))
print(fruites_tuple2)

#get a value 
print(fruites_tuple[1])

#cannot change value in tuple 
#fruites_tuple[1] = 'something else'

#Tuple with one value should have a trailing comma 
fruites_tuple3 = ('Apple', )
print(fruites_tuple3)

print(len(fruites_tuple3))

#deleteing tuple 
del fruites_tuple2 


# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = {'Apple', 'Orange', 'Mango'}
print(fruit_set)

#check if in set 
print('Apple' in fruit_set)

#adding to set 
fruit_set.add('Grape')
print(fruit_set)

#remove from set 
fruit_set.remove('Grape')
print(fruit_set)

#clear whole set 
fruit_set.clear()
print(fruit_set)


#delete set 
del fruit_set 
print(fruit_set)
