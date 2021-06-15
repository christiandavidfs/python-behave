from behave import *
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
import requests
 
Google_HOME = 'https://duckduckgo.com//'
searchtext= ''

 
@given('the Google home page is displayed')
def step_impl(context):
  context.browser.get(Google_HOME)

@when('the user grab a value from an API')
def step_impl(context):
  response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
  searchtex= response.json()['title']
  context.searchtext=str(searchtex)


@when('the user searches for API')
def step_impl(context):
  search_input = context.browser.find_element_by_name('q')
  search_input.send_keys(context.searchtext + Keys.RETURN)
 
@then('results are shown for API')
def step_impl(context):
  links_div = context.browser.find_element_by_id('links')
  assert len(links_div.find_elements_by_xpath('//div')) > 0
  search_input = context.browser.find_element_by_name('q')
  assert search_input.get_attribute('value') == 'AssertionError' #context.searchtext