from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us as false!')
def step_impl(context):
    assert context.failed is False

@then('behave will test it for us as true!')
def step_impl(context):
    assert context.failed is True
