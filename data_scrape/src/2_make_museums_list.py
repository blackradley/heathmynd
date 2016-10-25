"""  Make a list of the museums and their types. """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import helpers_list

ceremonial_counties_of_england = helpers_list.get_ceremonial_counties_of_england()

for county in ceremonial_counties_of_england:
    print '\nMaking museum data file\n---'
    wiki_file_name = '../download/List_of_museums_' + county + '.wiki'
    output_file_name = './data/List_of_museums_' + county + '.txt'

    with open(wiki_file_name, "r") as wiki_file, open(output_file_name,"w") as output_file:
        print 'Output to: ' + output_file_name
        output_file.write('name\tcounty\ttype\twikipedia_link\n')

        wiki_page = wiki_file.read()
    
        type_column = helpers_list.get_museum_type_column(wiki_page)
        # Get a list of the types
        types = helpers_list.get_museum_types(wiki_page, type_column)
        # Get a list of the museums
        museums = helpers_list.get_museums_list(wiki_page)
        # Merge the two lists in to one
        merged_list = zip(museums, types)
        for row in merged_list:
            name = row[0][0]
            link = row[0][1]
            type = row[1]
            classified_type = helpers_list.classify_type(type)
            print name
            output_file.write(name + '\t' + county + '\t' + classified_type + '\t' + link + '\n')

