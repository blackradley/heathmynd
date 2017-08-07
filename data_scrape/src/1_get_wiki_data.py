""" Get the county museum lists from wikipedia.

Doing it this way, rather than cutting and pasting ensures that the same
encoding is used as urllib2 uses."""

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import io
import requests  # for getting the pages from Wikipedia
import helpers_list

print '\nGet Wikipedia Data\n---'

COUNTIES_ENGLAND_CEREMONIAL = helpers_list.get_counties_england_ceremonial()

DATA = None
HEADERS = {'User-Agent' : 'ProjectHeathMynd (+http://www.blackradley.com/contact-us/)'}

for county in COUNTIES_ENGLAND_CEREMONIAL:
    url = 'https://en.wikipedia.org/wiki/List_of_museums_' + county
    response = requests.get(url)
    content = response.text
    county_museums_file_path = helpers_list.get_canonical_path_for(
        '../download/List_of_museums_' + county + '.htm')
    county_museums_file = io.open(county_museums_file_path, 'w', encoding='utf-8')
    county_museums_file.write(content)
    county_museums_file.close()
