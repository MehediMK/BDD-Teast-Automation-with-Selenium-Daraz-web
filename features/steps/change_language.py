from behave import *
from selenium import webdriver

# Note: open browser and browse daraz website in daraz_search file


@when('Click on "ভাষা" link from top menu bar')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="topActionSwitchLang"]/span').click()


@when('Click on "BN / Bengali"')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="lzdSwitchPop"]/div/div[1]/span').click()


@then('Close Browser')
def step_impl(context):
    context.driver.close()


@when('Click on "CHANGE LANGUAGE" link from top menu bar')
def step_impl(context):
    context.driver.find_element_by_id('topActionSwitchLang').click()


@when(u'Click on "EN / English"')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="lzdSwitchPop"]/div/div[2]').click()