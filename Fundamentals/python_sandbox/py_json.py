# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json 

#sample json 
userJSON = '{"first_name" : "Chamin" , "last_name" : "Nalinda", "age" : 30}'

#pass JSON to dictionary so Python can process
user = json.loads(userJSON)

print(user)
print(user['first_name'])

#pass dictionary to json 
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)