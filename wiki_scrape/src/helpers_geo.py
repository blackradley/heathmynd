'''
Helpers for getting the locations of places

Joe J Collins
31 March 2011
'''
import re # for regular expressions
import urllib # for url encoding
import urllib2 # for getting the gear from Wikipedia
import string
import simplejson

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
    # e.g. http://maps.googleapis.com/maps/api/geocode/json?address=Basildon%20Park,%20Berkshire&bounds=49.766807,-7.557160|56.474628,3.493652&region=uk
    address_string = (name + ', ' + county).replace(' ', '+')
    boundary_box_string =  __uk_boundry_box()
    google_url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + address_string + '&bounds=' + boundary_box_string + '&region=uk'
    print google_url
    google_request = urllib2.Request(google_url, data, headers)
    google_response = urllib2.urlopen(google_request)
    json = simplejson.loads(google_response.read())
    location = []
    # http://stackoverflow.com/questions/4639311/parsing-json-file-with-python-google-map-api
    if json['status'] == 'OK':
        for s in json['results']:
             lat = s['geometry']['location']['lat'] 
        for s in json['results']:
             lng = s['geometry']['location']['lng'] 
        location = [lat, lng]
    else:
        location = [0.0,0.0]
    return location

def __uk_boundry_box():
    # SV00 in the OS Grid (the origin)
    south_west_lat = 49.766807
    south_west_lng = -7.557160 
    # Somewhere in the North Sea
    north_east_lat = 56.474628
    north_east_lng = 3.493652 
    return str(south_west_lat) + ',' + str(south_west_lng) + '|' + str(north_east_lat) + ',' + str(north_east_lng)
