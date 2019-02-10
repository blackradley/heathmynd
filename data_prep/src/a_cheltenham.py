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
CODE_POINT_IN = os.path.join(package_directory, "../data/external/cheltenham-code-point.csv")
CODE_POINT_OUT = os.path.join(package_directory, "../data/interim/cheltenham-code-point.csv")
DEPRIVATION_IN = os.path.join(package_directory, "../data/external/cheltenham-deprivation.csv")
DEPRIVATION_OUT = os.path.join(package_directory, "../data/interim/cheltenham-deprivation.csv")

def main():
    """ Read the original csv files and produce simpler ones """
    simplify_code_point(CODE_POINT_IN, CODE_POINT_OUT)
    simplify_deprivation(DEPRIVATION_IN, DEPRIVATION_OUT)

def simplify_code_point(in_file_path, out_file_path):
    """ Get the postcode and convert the UK grid references to WGS84

    Ordnance Survey maintains the centroid of the postcode in UK
    grid reference.  Google Maps uses World Geodetic System (WGS84)
    so the UK grid reference need to be converted.  This is done
    mathematically.  Theoretically this isn't precise, but it is
    surely going to be precise enough for out purposes. """
    with open(in_file_path, "rb") as in_file, open(out_file_path, "wb") as out_file:
        code_point_reader = csv.reader(in_file, delimiter=",", quotechar='"')
        next(code_point_reader, None)  # skip the original headers
        code_point_writer = csv.writer(out_file)
        code_point_writer.writerow(["postcode", "latitude_bl", "longitude_bl",
                                    "latitude_tr", "longitude_tr"]) # write new headers
        for row in code_point_reader:
            postcode = __minify_postcode(row[0])
            eastings = int(row[2])
            northings = int(row[3])
            wgs84_coordinate = convert_lonlat([eastings], [northings]) # in the house, up the stairs
            longitude_bl = round(wgs84_coordinate[0][0], 5)
            latitude_bl = round(wgs84_coordinate[1][0], 5)
            eastings = eastings + 5
            northings = northings + 5
            wgs84_coordinate = convert_lonlat([eastings], [northings])
            longitude_tr = round(wgs84_coordinate[0][0], 5)
            latitude_tr = round(wgs84_coordinate[1][0], 5)
            code_point_writer.writerow([postcode, latitude_bl, longitude_bl,
                                        latitude_tr, longitude_tr])

def simplify_deprivation(in_file_path, out_file_path):
    """ Just get the postcode and the deprivation score

    I don't think we need terminated postcodes so I am only selecting the
    Live ones.  The Terminated postcodes are maintained by the ONS, I am
    assuming so they can do comparisons across time or something like that.
    The ONS uses a different set of geographic areas but they aren't so
    meaningful to people so I am going with postcodes. About 30% of the
    Cheltenham postcodes are terminated. """
    with open(in_file_path, "rb") as in_file, open(out_file_path, "wb") as out_file:
        deprivation_reader = csv.reader(in_file, delimiter=",", quotechar='"')
        next(deprivation_reader, None)  # skip the original headers
        deprivation_writer = csv.writer(out_file)
        deprivation_writer.writerow(["postcode", "rank", "decile"]) # write new headers
        for row in deprivation_reader:
            postcode_status = row[1]
            if postcode_status == "Live":
                postcode = __minify_postcode(row[0])
                rank = row[4]
                decile = row[5]
                deprivation_writer.writerow([postcode, rank, decile])

def __minify_postcode(postcode):
    """ Remove the spaces and change to uppercase

    ...so the postcodes can be compared.  Strictly the postcode should be
    formatted with a space in front of the last three characters (the
    inward code) but I just need to compare them so removing the spaces
    and forcing them to uppercase makes them look the same. """
    postcode = postcode.replace(" ", "") # remove the space
    postcode = postcode.upper() # make uppercase
    return postcode

if __name__ == "__main__":
    main()
