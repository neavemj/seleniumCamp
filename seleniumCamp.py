#!/usr/bin/env python

from selenium import webdriver

# use webdriver for camp website

driver = webdriver.Firefox()
driver.get("http://www.parkstay.vic.gov.au/great-otway-national-park-west-kennett-river-to-princetown")

# helper functions

def select_in_dropdown(menu, selection):
    for option in menu.find_elements_by_tag_name("option"):
        if option.text == selection:
            option.click()
            return

# change date

def change_date(day, month_year):
    driver.find_element_by_class_name("pseudo").click()
    date_picker = driver.find_element_by_class_name("wdDatePicker_calendar")

    dropdown = date_picker.find_element_by_tag_name("select")
    select_in_dropdown(dropdown, month_year)

    # need re-find the calendar element to avoid "element no longer attached to DOM" error
    date_picker = driver.find_element_by_class_name("wdDatePicker_calendar")
    day_elem = date_picker.find_elements_by_xpath("//b[text()='%s']" % day)
    day_elem[0].click()

# check if site booked

def check_if_booked(site):
    site_elem = driver.find_elements_by_xpath("//a[text()='%s']" % site)
    grand_parent = site_elem[0].find_elements_by_xpath("../..")
    decendents = grand_parent[0].find_elements_by_xpath(".//*")
    for child in decendents:
        if child.get_attribute("class") == "price sold":
            return True
        elif child.get_attribute("class") == "price":
            return False


change_date("28", "July 2016")
