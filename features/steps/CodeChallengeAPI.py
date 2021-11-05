from behave import *
from behave import given, when, then
import requests
import json
 
searchtext= ''

 
@given('the API is UP')
def step_impl(context):
  response = requests.get('https://api.duckduckgo.com/')
# print request object
  print(response.url)
# print status code
  print(response.status_code)
  assert str(response.status_code)=='200'

@when('the user gets images list')
def step_impl(context):
  searchstring='dogs'
  response = requests.get('https://api.duckduckgo.com/?q='+searchstring+'&iax=images&ia=images&format=json')
  context.pretty_json = json.loads(response.text)
  f = open('fullimageresult.txt','w')
  print(context.pretty_json, file=f)

@Then('print results')
def step_impl(context):
  with open('fullimageresult.txt') as json_file:
    data = json.load(json_file)
  names = json_extract(data.json(), 'text')
  print(names)

  f = open('imageresult.txt','w')
  print(data, file=f)
