"""  Get location data for each of the museums. """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import helpers_list
import helpers_geo

ceremonial_counties_of_england = helpers_list.get_counties_england_ceremonial()
ceremonial_counties_of_england = ['in_Bristol', 'in_Cornwall', 'in_Devon', 
        'in_Dorset', 'in_Gloucestershire', 'in_Somerset', 'in_Wiltshire']
ceremonial_counties_of_england = ['in_Leicestershire']
ceremonial_counties_of_england = ['in_Essex']

for county in ceremonial_counties_of_england:
    print '\n---'
    museum_list_file_name = './data/interim/List_of_museums_' + county + '.txt'
    output_file_name = './data/interim/List_of_museums_' + county + '_.txt'
    print 'Output to: ' + output_file_name

    with open(museum_list_file_name, "r") as wikipedia_file, open(output_file_name, "w", "utf-8") as output_file:
        output_file.write('name\tcounty\ttype\twikipedia_link\n')

output_file_name = '../data/interim/List_of_museums.txt'
print 'Output to: ' + output_file_name
output_file = open(output_file_name,"wb")
output_file.write('name\tlink\ttype\ticon\tlat\tlng\tcounty\n')



# open a file for output date
for county in counties:
    # open the wiki page
    wiki_file_name = '../download/List_of_museums_in_' + county + '.wiki'
    print 'Input from: ' + wiki_file_name
    the_page = open(wiki_file_name, "r").read()
    
    type_column = helpers_list.get_museum_type_column(the_page)
    # Get a list of the types
    types = helpers_list.get_museum_types(the_page, type_column)
    # Get a list of the museums
    museums = helpers_list.get_museums_list(the_page)
    # Merge the two lists in to one
    merged_list = zip(museums, types)
    # Write out the file, rearranging and geocoding as you go
    
    for row in merged_list:
        name = row[0][0]
        link = row[0][1]
        type = row[1]
        classified_type = helpers_list.classify_type(type)
        iconized_type = helpers_list.iconize_type(classified_type)
        location = helpers_geo.get_wikipedia_location(link)
        if location[0] == 0.0: # then there is no location in Wikipedia
            location = helpers_geo.get_google_location(name, county)
        lat = location[0]
        lng = location[1]
        print name
        output_file.write(name + '\t' + link + '\t' + classified_type + '\t' + iconized_type +
                   '\t' + str(lat)  + '\t' + str(lng)  + '\t' + county + '\n')
    
output_file.close()
