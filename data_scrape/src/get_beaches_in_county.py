'''
Get the beaches in a county

Joe J Collins
2 April 2011
'''
from xml.dom.minidom import parse

county = 'Cornwall'
file = '../test_data/Beaches_of_' + county + '.xml'

dom = parse(file) # parse an XML file by name

beaches = dom.getElementsByTagName("Placemark")

file_name = '../data/Beaches_of_' + county + '.txt'
file = open(file_name,"wb")
file.write('name\tlink\ttype\tlat\tlng\tcounty\n')

for beach in beaches:
    name = beach.getElementsByTagName("name")[0].firstChild.wholeText
    type = 'beach'
    link = name.replace(' ', '_')
    location = beach.getElementsByTagName("coordinates")[0].firstChild.wholeText
    coords = location.split(',')
    lat = coords[1]
    lng = coords[0]
    file.write(name + '\t' + link + '\t' + type + '\t' + str(lat)  + '\t' + str(lng)  + '\t' + county + '\n')
file.close()