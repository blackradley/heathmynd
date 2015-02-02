'''
Helpers for getting the locations of places

Joe J Collins
31 March 2011
'''
import re # for regular expressions
import urllib2 # for getting the gear from Wikipedia
import string
import simplejson

data = None
headers = { 'User-Agent' : 'ProjectHopeBowdler (+http://www.blackradley.com/contact-us/)' }

def get_wiki_location(link):
    kml_url = 'http://toolserver.org/~para/cgi-bin/kmlexport?article=' + link.replace('&', '%26')
    # I know replace('&', '%26') is naff, but I can't be arsed to think about encoding.
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
    address = (name + ', ' + county).replace(' ', '+').replace('&', '%26')
    google_url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&sensor=false&bounds=49.766807,-7.557160|56.474628,3.493652&region=uk'
    # restricted by region and bounding box 
    # 49.766807,-7.557160 is SV00 in the OS Grid (the origin)
    # 56.474628,3.493652 is somewhere in the North Sea
    
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
