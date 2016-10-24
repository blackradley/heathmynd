'''
Get the coordinates of a wikipage from some KML.

Joe Collins
24 October 2016

'''
import os
import urllib # for url encoding
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromedriver = "../chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

query = "Aythorpe Roding Windmill, Essex"
html_url = "http://www.google.com/search?q=%s&num=1&hl=en&start=0&cr=countryUK|countryGB" % (urllib.quote_plus(query))
driver.get(html_url)

driver.close()

