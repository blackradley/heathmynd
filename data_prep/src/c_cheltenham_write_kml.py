""" Create tower blocks """
import jinja2
import csv
import os
import xml.dom.minidom

PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BAR_CHART_CSV = os.path.join(PACKAGE_DIRECTORY, "../data/interim/bar_chart_data.csv")
OUTPUT_KML = os.path.join(PACKAGE_DIRECTORY, "../data/processed/cheltenham_deprivation.kml")

def main():
    """ Read the csv and write out KML """
    order = ['postcode', 'latitude_bl', 'longitude_bl', 'latitude_tr',
             'longitude_tr', 'postcode:1', 'rank', 'decile']
    csv_reader = csv.DictReader(open(BAR_CHART_CSV), order)
    create_KML(csv_reader, OUTPUT_KML, order)

# def extractAddress(row):
#   # This extracts an address from a row and returns it as a string. This requires knowing
#   # ahead of time what the columns are that hold the address information.
#   return '%s,%s,%s,%s,%s' % (row['Address1'], row['Address2'], row['City'], row['State'], row['Zip'])

# def createPlacemark(kmlDoc, row, order):
#   # This creates a  element for a row of data.
#   # A row is a dict.
#   placemarkElement = kmlDoc.createElement('Placemark')
#   extElement = kmlDoc.createElement('ExtendedData')
#   placemarkElement.appendChild(extElement)
  
#   # Loop through the columns and create a  element for every field that has a value.
#   for key in order:
#     if row[key]:
#       dataElement = kmlDoc.createElement('Data')
#       dataElement.setAttribute('name', key)
#       valueElement = kmlDoc.createElement('value')
#       dataElement.appendChild(valueElement)
#       valueText = kmlDoc.createTextNode(row[key])
#       valueElement.appendChild(valueText)
#       extElement.appendChild(dataElement)
  
#   pointElement = kmlDoc.createElement('Point')
#   placemarkElement.appendChild(pointElement)
#   coordinates = geocoding_for_kml.geocode(extractAddress(row))
#   coorElement = kmlDoc.createElement('coordinates')
#   coorElement.appendChild(kmlDoc.createTextNode(coordinates))
#   pointElement.appendChild(coorElement)
#   return placemarkElement

def create_KML(csv_reader, file_name, order):
    """ This constructs the KML document from the CSV file. """

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    print env.get_template("feedtemplate.xml").render(items=get_list_of_items())

    # kml_doc = xml.dom.minidom.Document()
    # kml_element = kml_doc.createElementNS('http://earth.google.com/kml/2.2', 'kml')
    # kml_element.setAttribute('xmlns', 'http://earth.google.com/kml/2.2')
    # kml_element = kml_doc.appendChild(kml_element)
    # document_element = kml_doc.createElement('Document')
    # folder_element = kml_doc.createElement('Folder')
    # document_element.appendChild(folder_element)
    # kml_element.appendChild(document_element)

    # Skip the header line.
    # csv_reader.next()
    # for row in csv_reader:
    #     placemarkElement = createPlacemark(kmlDoc, row, order)
    #     documentElement.appendChild(placemarkElement)

    kml_file = open(file_name, 'w')
    kml_file.write(kml_doc.toprettyxml('  ', newl='\n', encoding='utf-8'))



if __name__ == '__main__':
  main()
