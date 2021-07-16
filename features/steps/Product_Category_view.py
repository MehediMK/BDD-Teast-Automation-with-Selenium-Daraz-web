from behave import *
from selenium import webdriver


@when('click on "Traditional Laptops" from "Related Categories" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/a[1]').click()


@when('click on "Gaming Laptops" from "Related Categories" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/a[2]').click()


@when('click on "Macbooks" from "Related Categories" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/a[7]').click()


@when('click on "Routers" from "Related Categories" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/a[3]').click()


@when('click on "Basic Micep" from "Related Categories" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/a[6]').click()


@when('click on "Basic" from "Related Categories" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/a[4]').click()

    
