"""  Make a list of the museums and their types. """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import io
import helpers_list

COUNTIES_ENGLAND_CEREMONIAL = helpers_list.get_counties_england_ceremonial()

j = 0 # Counter for all the museums in England
for county in COUNTIES_ENGLAND_CEREMONIAL:
    print '\n---'
    wikipedia_file_name = '../data/raw/List_of_museums_' + county + '.htm'
    wikipedia_file_path = helpers_list.get_canonical_path_for(wikipedia_file_name)
    output_file_name = '../data/interim/List_of_museums_' + county + '.txt'
    output_file_path = helpers_list.get_canonical_path_for(output_file_name)
    print 'Output to: ' + output_file_name
    with io.open(wikipedia_file_path, 'r', encoding='utf-8') as wikipedia_file, \
            io.open(output_file_path, 'w', encoding='utf-8') as output_file:
        header = unicode('name\tcounty\ttype\twikipedia_link\n')
        output_file.write(header)
        wikipedia_page = wikipedia_file.read()
        museums_list = helpers_list.get_museums_list(wikipedia_page)
        i = 0
        for row in museums_list:
            i += 1 # counter for displaying progress in county
            j += 1 # counter for displaying total number of museums
            name = row['name']
            link = row['wikipedia_link']
            museum_type = row['type']
            classified_type = helpers_list.classify_type(museum_type)
            print '{},'.format(i), # print progress, the last comma keeps the print on the same line
            output_file.write(name + '\t' + county + '\t' + classified_type + '\t' + link + '\n')
        print '\nCumulative total: {}'.format(j)

# The Arts Council says there are 1,600 
# http://webarchive.nationalarchives.gov.uk/20160204101926/http://www.artscouncil.org.uk/media/uploads/pdf/a_review_of_research.pdf
#   
