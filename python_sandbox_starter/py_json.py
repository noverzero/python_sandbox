# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json
 
# sample json

userJSON = '{"first_name": "John", "last_name": "Doe", "age: 32"}'

# Parse to dict

user = json.loads(userJSON)

print(user)
