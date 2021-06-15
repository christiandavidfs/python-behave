from selenium import webdriver
 
def before_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(100000)
 
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()