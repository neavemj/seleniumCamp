#!/usr/bin/env python

from selenium import webdriver
from time import sleep

# use webdriver for camp website

driver = webdriver.Firefox()
driver.get("http://www.parkstay.vic.gov.au/great-otway-national-park-west-kennett-river-to-princetown")

# helper functions

def select_in_dropdown(menu, selection):
    for option in menu.find_elements_by_tag_name("option"):
        if option.text == selection:
            option.click()
            return

# main functions

def change_date(day, month_year):
    # click on calendar to make it appear and give access
    driver.find_element_by_class_name("pseudo").click()

    # change month / year from dropdown menu
    date_picker = driver.find_element_by_class_name("wdDatePicker_calendar")
    dropdown = date_picker.find_element_by_tag_name("select")
    select_in_dropdown(dropdown, month_year)

    # change day in calendar
    # need to re-find the calendar element to avoid "element no longer attached to DOM" error
    date_picker = driver.find_element_by_class_name("wdDatePicker_calendar")
    day_elem = date_picker.find_elements_by_xpath("//b[text()='%s']" % day)
    day_elem[0].click()


def check_if_booked(site):
    # first find site, them move up tree to get to other elements
    site_elem = driver.find_elements_by_xpath("//a[text()='%s']" % site)
    grand_parent = site_elem[0].find_elements_by_xpath("../..")
    decendents = grand_parent[0].find_elements_by_xpath(".//*")
    for child in decendents:
        if child.get_attribute("class") == "price sold":
            return True
        if child.get_attribute("class") == "price":
            return False


change_date("28", "July 2016")
# need to add a sleep or else next function has nothing to click on
# should to this better somehow - wait for element to be present or something..
sleep(1)
print check_if_booked("Blanket Bay Campground site 01")

"""
# could do a while loop to keep refreshing page until the site is available
while True:
    if check_if_booked("Aire River Campground site 04"):
        driver.refresh()
        sleep(1)
    else:
        book_site()
        break
"""

