from behave import *
from selenium import webdriver


@given('Open Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


@given('Browse Daraz Website')
def step_impl(context):
    context.driver.get('https://www.daraz.com.bd/')


@when('Type {mk} search bar')
def step_impl(context,mk):
    context.driver.find_element_by_id('q').send_keys(mk)


@when('Click/Press Enter on Search Button')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button').click()
    


@when('Count all product in first page')
def step_impl(context):
    child_path = context.driver.find_elements_by_class_name("c2prKC")
    count = 0
    for child in child_path:
        count += 1
    print(count)


@then('Close Chrome Browser')
def step_impl(context):
    context.driver.close()


@when('Assert how many items found')
def step_impl(context):
    items_assert = context.driver.find_element_by_class_name("c1DXz4").is_displayed()
    if items_assert == "True":
        assert items_assert,"Product found"
     


@when('Get total search item found')
def step_impl(context):
    items_assert = context.driver.find_element_by_class_name("c1DXz4").text
    print(items_assert)

