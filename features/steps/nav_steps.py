import os
from behave import given, when, then
from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@given('flaskr is setup')
def flask_setup(context):
    set_driver(context.browser)
    go_to('http://' + os.environ['CODIO_HOSTNAME'] + '-5000.codio.io/')
    WebDriverWait(context.browser, 5)
    assert context.client and context.db

@when('I click on "{link}"')
def step_impl(context, link):
    set_driver(context.browser)
    click(link)
    WebDriverWait(context.browser, 5)

@then('I should be redirected to the "{page_title}" page')
def step_impl(context, page_title):
    assert page_title in context.browser.title
