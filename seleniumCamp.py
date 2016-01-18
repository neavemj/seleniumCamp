#!/usr/bin/env python

from selenium import webdriver
import os

# use webdriver for camp website

driver = webdriver.Firefox()
driver.get("http://www.parkstay.vic.gov.au/great-otway-national-park-west-kennett-river-to-princetown")

# change date

def change_date(new_date):
    driver.find_element_by_class_name("pseudo").click()
    date_picker = driver.find_element_by_class_name("wdDatePicker_calendar")
    rows = date_picker.find_element_by_tag_name("tr")
    columns = date_picker.find_element_by_tag_name("td")
    for cell in columns:
        if cell.text == "20":
            cell.click()

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


change_date("none")
