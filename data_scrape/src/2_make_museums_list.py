"""  Make a list of the museums and their types. """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import codecs
import helpers_list
import helpers_list

ceremonial_counties_of_england = helpers_list.get_ceremonial_counties_of_england()

number_of_museums = 0
for county in ceremonial_counties_of_england:
    print '\n---'
    wikipedia_file_name = '../download/List_of_museums_' + county + '.htm'
    output_file_name = './data/List_of_museums_' + county + '.txt'
    print 'Output to: ' + output_file_name
    with open(wikipedia_file_name, "r") as wikipedia_file, codecs.open(output_file_name, "w", "utf-8") as output_file:
        output_file.write('name\tcounty\ttype\twikipedia_link\n')
        wikipedia_page = wikipedia_file.read()
        museums_list = helpers_list.get_museums_list(wikipedia_page)
        i = 0
        for row in museums_list:
            i += 1 # counter for displaying progress
            number_of_museums += 1
            name = row['name']
            link = row['wikipedia_link']
            
            type = row['type']
            classified_type = helpers_list.classify_type(type)
            print '{},'.format(i), # print progress, the last comma keeps the print on the same line
            output_file.write(name + '\t' + county + '\t' + classified_type + '\t' + link + '\n')
print 'Total number of musuems: ' + str(number_of_museums)            