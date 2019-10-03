import json
import requests

# POST request have everything a GET request has + json or xml
    # We'll cover json

headers = {'Content-Type': 'application/json'}
path = 'http://api.postcodes.io/postcodes/'
arguements = ''

json_body = json.dumps({"postcodes": ["E14 6GT", "TN279NF", "NE30 1DP"]})

multi_post_codes = requests.post(path, headers = headers, data = json_body)

dict_multi_results = multi_post_codes.json()['result']

#print(dict_multi_results)
print(dict_multi_results[1])