""" Create tower blocks """
import csv
import os
import jinja2
# import xml.dom.minidom

PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BAR_CHART_CSV = os.path.join(PACKAGE_DIRECTORY, "../data/interim/bar_chart_data.csv")
OUTPUT_KML = os.path.join(PACKAGE_DIRECTORY, "../data/processed/cheltenham_deprivation.kml")

def main():
    """ Read the csv and write out KML """
    order = ['postcode', 'latitude_bl', 'longitude_bl', 'latitude_tr',
             'longitude_tr', 'postcode:1', 'rank', 'decile']
    csv_reader = csv.DictReader(open(BAR_CHART_CSV), order)
    create_KML(csv_reader, OUTPUT_KML, order)

def create_KML(csv_reader, file_name, order):
    """ This constructs the KML document from the CSV file. """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(PACKAGE_DIRECTORY))
    postcodes = iter(csv_reader)
    kml = env.get_template("cheltenham_template.xml").render(postcodes=postcodes)
    kml_file = open(file_name, 'w')
    kml_file.write(kml)
    #kml_file.write(kml_doc.toprettyxml('  ', newl='\n', encoding='utf-8'))




if __name__ == '__main__':
    main()
