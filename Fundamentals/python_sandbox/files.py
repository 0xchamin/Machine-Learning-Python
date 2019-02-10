# Python has functions for creating, reading, updating, and deleting files.

#Open file 

myfile = open('myfile.txt', 'w')

#get info 
print('Name: ', myfile.name)
print('Is Closed: ', myfile.closed)
print('Openning mode : ', myfile.mode)

#write to file 

myfile.write('I love Python')

myfile.write(' I love Sri Lanka')
myfile.close()

#Append to file 
myfile = open('myfile.txt', 'a') # 'a' for append mode 
myfile.write(' I also like JS')


#read from files 

myfile = open('myfile.txt', 'r+')
text = myfile.read(100)
print(text)