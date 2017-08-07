"""  Make a list of the museums and their types. """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import io
import helpers_list

COUNTIES_ENGLAND_CEREMONIAL = helpers_list.get_counties_england_ceremonial()

<<<<<<< HEAD
number_of_museums = 0
for county in ceremonial_counties_of_england:
=======
j = 0 # Counter for all the museums in England
for county in COUNTIES_ENGLAND_CEREMONIAL:
>>>>>>> a42a2f9a61e7213f51836000303a2165cd49e261
    print '\n---'
    wikipedia_file_name = '../download/List_of_museums_' + county + '.htm'
    wikipedia_file_path = helpers_list.get_canonical_path_for(wikipedia_file_name)
    output_file_name = './data/List_of_museums_' + county + '.txt'
    output_file_path = helpers_list.get_canonical_path_for(output_file_name)
    print 'Output to: ' + output_file_name
    with io.open(wikipedia_file_path, 'r') as wikipedia_file, \
            io.open(output_file_path, 'w', encoding='utf-8') as output_file:
        header = unicode('name\tcounty\ttype\twikipedia_link\n')
        output_file.write(header)
        wikipedia_page = wikipedia_file.read()
        museums_list = helpers_list.get_museums_list(wikipedia_page)
        i = 0
        for row in museums_list:
<<<<<<< HEAD
            i += 1 # counter for displaying progress
            number_of_museums += 1
=======
            i += 1 # counter for displaying progress in county
            j += 1 # counter for displaying total number of museums
>>>>>>> a42a2f9a61e7213f51836000303a2165cd49e261
            name = row['name']
            link = row['wikipedia_link']
            museum_type = row['type']
            classified_type = helpers_list.classify_type(museum_type)
            print '{},'.format(i), # print progress, the last comma keeps the print on the same line
            output_file.write(name + '\t' + county + '\t' + classified_type + '\t' + link + '\n')
<<<<<<< HEAD
print 'Total number of musuems: ' + str(number_of_museums)            
=======
        print '\nCumulative total: {}'.format(j)
>>>>>>> a42a2f9a61e7213f51836000303a2165cd49e261
