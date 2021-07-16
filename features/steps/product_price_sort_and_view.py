from behave import *
from selenium import webdriver


@when('Select/click on "Price low to heigh" from "Short By" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div').click()
    context.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[2]/div').click()
        

@when('Select/click on  "Price heigh to low" from "Short By" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div').click()
    context.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[3]/div').click()
        

@when('Select/click on "Bast Match" from "Short By" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div').click()
    context.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]/div').click()


@when('click on "list view icon" from "View" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[4]/span[2]/i').click()


@when('click on "grid view icon" from "View" area')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[4]/span[2]/i').click()
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[4]/span[1]/i').click()




    