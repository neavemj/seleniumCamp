#!/usr/bin/env python

from selenium import webdriver
import os

# use webdriver for camp site

driver = webdriver.Firefox()
driver.get("http://www.parkstay.vic.gov.au/great-otway-national-park-west-kennett-river-to-princetown")

# change date


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

print(check_if_booked("Blanket Bay Campground site 01"))
print(check_if_booked("Aire River East Campground site 03"))