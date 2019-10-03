import requests

# get is a server request that sends :
    # headers, path and arguments
        # headers are meta data slightly hidden - things like screen size, device info and other
        # path is the url section that determines where to senf info - location on the internet
        # arguements are the information you send. (as is header)

headers = ''
path = 'http://api.postcodes.io/postcodes/'
arguements = 'E146GT'

post_code_req = requests.get(path + arguements)

print(post_code_req)

# print(post_code_req.status_code)
# print(post_code_req.headers)
print(type(post_code_req.content))
print(type(post_code_req.json())) #--> pasrses this into a dictionary
dict_of_request = post_code_req.json( ) # --> then you can use it
