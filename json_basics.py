import json

car_data = {
    'engine': 'electric',
    'brand' : 'Peugeot',
    'price' : 13000,
    'model' : 'Ze'
}

print(type(car_data))

# dict --> str - using json.dumps(dict)
car_data_json_string = json.dumps(car_data)

print(car_data_json_string)
print(type(car_data_json_string))

# write a json file
car_data = {
    'engine': 'electric',
    'brand' : 'Peugeot',
    'price' : 13000,
    'model' : 'Ze'
}

with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_data, jsonfile)
    # json.dump(arg1, arg1) --> .json file
        # arg1 is dictionary
        # arg2 is the file to dumo the json