'''
Remove ExtendedData sections from a KML file 

Joe J Collins
17 May 2011
'''
from xml.dom.minidom import parseString
import urllib2 # for getting the gear from Fusion tables

data = None
headers = { 'User-Agent' : 'ProjectHeathMynd (+http://www.blackradley.com/contact-us/)' }
types = ["Arts", "Historic", "Industrial", "Local", "Multiple", "Other", "Transport" ]

for type in types:
    # Get the KML from the Fusion table
    url = "http://www.google.com/fusiontables/exporttable?query=select+col0%2C+col1%2C+col2%2C+col6%2C+col3%2C+col4%2C+col5+from+614442+where+col2+%3D+'" + type + "'&o=kmllink&g=col3"
    print url
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    the_kml = response.read()
    # Remove the Fusion Tables Folder
    the_kml = the_kml.replace('<Folder id=\"Fusiontables\">', '')
    the_kml = the_kml.replace('<name>Fusiontables folder</name>', '')
    the_kml = the_kml.replace('</Folder>', '')
    the_kml = the_kml.replace('http://maps.google.com/mapfiles/kml/paddle/red-blank_maps.png',
                              'http://swmuseums.blackradleysystems.com/static/museums/' + type.lower() + '.png');
    # Remove the ExtendedData
    dom = parseString(the_kml) # parse the KML string
    place_marks = dom.getElementsByTagName("Placemark")
    for place_mark in place_marks:
        extended_data = place_mark.getElementsByTagName("ExtendedData")[0]
        place_mark.removeChild(extended_data)
        
    file = open('../../web_app/src/static/museums/' + type.lower() + '.xml', 'wb')
    file.write(dom.toxml())
    file.close()

