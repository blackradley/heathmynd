'''
Helpers for getting the locations of places

Joe J Collins
31 March 2011
'''
import re # for regular expressions
import urllib # for url encoding
import urllib2 # for getting the gear from Wikipedia
import string

data = None
headers = { 'User-Agent' : 'HeathMynd (+http://www.blackradley.com/contact-us/)' }

def get_wikipedia_location(wikipedia_link):
    wikipedia_link = urllib.quote_plus(wikipedia_link)
    kml_url = 'http://toolserver.org/~para/cgi-bin/kmlexport?article=' + wikipedia_link
    kml_request = urllib2.Request(kml_url, data, headers)
    kml_response = urllib2.urlopen(kml_request)
    kml = kml_response.read()
    coordinates = re.search('(?<=<coordinates>)(.*?)(?=</coordinates>)', kml) # <coordinates>-0.46408,52.13607,0</coordinates>
    lat = lng = 0.0
    if coordinates != None:
        lat = string.split(coordinates.group(), ',')[1]
        lng = string.split(coordinates.group(), ',')[0]
        lat = float(lat)
        lng = float(lng)
    return [lat, lng]

def get_google_location(name, county):
    # e.g. https://www.google.co.uk/search?q=A+La+Ronde,+Devon&num=1&hl=en&start=0&cr=countryUK%7CcountryGB
    query = name + ", " + county
    html_url = "http://www.google.com/search?q=%s&num=1&hl=en&start=0&cr=countryUK|countryGB" % (urllib.quote_plus(query))
    html_request = urllib2.Request(html_url, data, headers)
    html_response = urllib2.urlopen(html_request)
    html = html_response.read()
    location = re.search('ll=\d+\.\d+,(-|)\d+\.\d+', html)
    location = location.group(0)
    if location.isspace():
        location = [0.0,0.0]
    else:
        location = location[3:].split(',')
        location = [float(i) for i in location]
    return location

def __uk_boundry_box():
    # SV00 in the OS Grid (the origin)
    south_west_lat = 49.766807
    south_west_lng = -7.557160 
    # Somewhere in the North Sea
    north_east_lat = 56.474628
    north_east_lng = 3.493652 
    return str(south_west_lat) + ',' + str(south_west_lng) + '|' + str(north_east_lat) + ',' + str(north_east_lng)
