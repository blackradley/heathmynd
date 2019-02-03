""" Prepare files for Sqlite

Sqlite will import csv files automatically if they
have an approriate header.  Sqlite will make assumptions
about the data so it is best that the column which 
we are going to join on is in the same format, so the
postcode needs to be formated similarly in all the files. """
import os
import csv
from convertbng.util import convert_bng, convert_lonlat

package_directory = os.path.dirname(os.path.abspath(__file__))
CODE_POINT_IN = os.path.join(package_directory, "../data/raw/cheltenham-code-point.csv")
CODE_POINT_OUT = os.path.join(package_directory, "../data/interim/cheltenham-code-point.csv")

def main():
    """ Read the original csv files and produce simpler ones """
    simplify_code_point(CODE_POINT_IN, CODE_POINT_OUT)
    
def simplify_code_point(in_file_path, out_file_path):
    with open(in_file_path, "rb") as in_file, open(out_file_path, "wb") as out_file:
        code_point_reader = csv.reader(in_file, delimiter=",", quotechar='"')
        next(code_point_reader, None)  # skip the headers
        code_point_writer = csv.writer(out_file)
        for row in code_point_reader:
            postcode = row[0].replace(" ", "") # remove the space
            postcode = postcode.upper()
            eastings = int(row[2])
            northings = int(row[3])
            wgs84_coordinate = convert_lonlat([eastings], [northings]) # in the house and up the stairs
            latitude = wgs84_coordinate[0]
            longitude = wgs84_coordinate[1]
            code_point_writer.writerow([postcode, latitude, longitude])



if __name__ == "__main__":
    main()