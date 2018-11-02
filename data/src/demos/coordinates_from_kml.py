'''
Get the coordinates of a wikipage from some KML.

Joe Collins
26 March 2011

'''
import re # for regular expressions
import string
kml = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.1">
<Document>
	<name><![CDATA[Bedford Museum & Art Gallery]]></name>
	<open>1</open>
	<Folder>
		<name><![CDATA[External links]]></name>
		<open>1</open>
		<Placemark>
			<name><![CDATA[Bedford Museum & Art Gallery]]></name>
			<Point>
				<coordinates>-0.46408,52.13607,0</coordinates>
			</Point>
			<Snippet></Snippet>
			<description><![CDATA[<br>Source: Wikipedia article <a href="http://en.wikipedia.org/wiki/Bedford_Museum_&_Art_Gallery">Bedford Museum & Art Gallery</a>]]></description>
		</Placemark>
	</Folder>
</Document>
</kml>'''
coordinates = re.search('(?<=<coordinates>)(.*?)(?=</coordinates>)', kml) # <coordinates>-0.46408,52.13607,0</coordinates>

lat = lng = None
if coordinates != None:
    lat = string.split(coordinates.group(), ',')[1]
    lng = string.split(coordinates.group(), ',')[0]

print "lat:" + lat + " Lng:" + lng
raw_input("Press ENTER to exit")


