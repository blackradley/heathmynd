""" Get the county museum lists from wikipedia. 

Doing it this way, rather than cutting and pasting ensures that the same
encoding is used as urllib2 uses."""

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import helpers_list
import urllib2 # for getting the pages from Wikipedia

print '\nGet Wikipedia Data\n---'

ceremonial_counties_of_england = helpers_list.get_ceremonial_counties_of_england()

data = None
headers = { 'User-Agent' : 'ProjectHeathMynd (+http://www.blackradley.com/contact-us/)' }

for county in ceremonial_counties_of_england:
    url = 'http://en.wikipedia.org/wiki/Special:Export/List_of_museums_' + county
    print url
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    content = response.read()
    file = open('../download/List_of_museums_' + county + '.wiki', 'wb')
    file.write(content)
    file.close()
