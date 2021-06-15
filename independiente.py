
# import requests module
import requests

# Making a get request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# print response
# print(response)

# print json content
itemvalue= response.json()['title']
print (itemvalue)

