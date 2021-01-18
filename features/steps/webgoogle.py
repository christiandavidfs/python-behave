from behave import *
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
 
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'
 
@given('the DuckDuckGo home page is displayed')
def step_impl(context):
  context.browser.get(DUCKDUCKGO_HOME)
 
@when('the user searches for "{searchtext}"')
def step_impl(context, searchtext):
  search_input = context.browser.find_element_by_name('q')
  search_input.send_keys(searchtext + Keys.RETURN)
 
@then('results are shown for "{searchresult}"')
def step_impl(context, searchresult):
  links_div = context.browser.find_element_by_id('links')
  assert len(links_div.find_elements_by_xpath('//div')) > 0
  search_input = context.browser.find_element_by_name('q')
  assert search_input.get_attribute('value') == searchresult