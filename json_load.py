# Here we load/decode json
import json

with open('new_json_file.json', 'r') as jsonfile: # r is the default value
    # convert ot a dictionary
    car_dict = json.load(jsonfile)
    print(car_dict)
    print(type(car_dict))
    print(car_dict['brand'])