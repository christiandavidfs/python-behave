from behave import *
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import re

 
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'
 
@given('the DuckDuckGo home page is loaded')
def step_impl(context):
  context.browser.get(DUCKDUCKGO_HOME)
 
@when('the user searches for the name "{searchtext}"')
def step_impl(context, searchtext):
  search_input = context.browser.find_element_by_name('q')
  search_input.send_keys(searchtext + Keys.RETURN)

@then('results are shown for the column "{searchresult}"')
def step_impl(context, searchresult):
  links_div = context.browser.find_element_by_link_text(searchresult)
  assert links_div

@then('results are shown for the column2 "{searchresult2}"')
def step_impl(context, searchresult2):
  links_div2 = context.browser.find_elements_by_xpath("//*[contains(text(), '"+ searchresult2 +"')]")
  assert links_div2

@then('an image is visible')
def step_impl(context):
  element = context.browser.find_element_by_class_name('module--about__img') #this element is visible
  assert element

@when('the user goes to the theme section and make changes in themes')
def step_impl(context):
  #context.browser.get(DUCKDUCKGO_HOME+'settings#theme')
  context.browser.find_element_by_xpath("/html/body/div/div[1]/div/a").click()
  context.browser.find_element_by_xpath("/html/body/div/div[4]/ul/ul[1]/li[2]/a").click() 
  context.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/form/div/div/div[6]").click() 
  context.browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div[1]/div[1]/div[3]/a").click()
  
  
  @then('the color is dark')
  def step_impl(context):
    element = context.browser.find_element_by_id('pg-index')
    background=element.value_of_css_property('background-color')
    r,g,b = map(int, re.search(
               r'rgb\((\d+),\s*(\d+),\s*(\d+)', background).groups())
    color = '#%02x%02x%02x' % (r, g, b)
    assert color=='#222222'

  @when('the user goes to the all settings section')
  def step_impl(context):
  #context.browser.get(DUCKDUCKGO_HOME+'settings#theme')
    context.browser.find_element_by_xpath("/html/body/div/div[1]/div/a").click()
    context.browser.find_element_by_xpath("/html/body/div/div[4]/ul/ul[1]/li[3]/a").click() 

  @when('change the languague')
  def step_impl(context):
  #context.browser.get(DUCKDUCKGO_HOME+'settings#theme')   
    context.browser.find_element_by_xpath("//*[@id='setting_kad']").click() 
    context.browser.find_element_by_xpath("//*[@id='setting_kad']/option[28]").click()

  @then('the languague is español (Chile)')
  def step_impl(context):
  #context.browser.get(DUCKDUCKGO_HOME+'settings#theme')   
    get_value=context.browser.find_element_by_xpath("//*[@id='setting_kad']")
    dropdown_value = get_value.get_attribute("value")
    #print(dropdown_value)
    assert dropdown_value=='es_CL'
