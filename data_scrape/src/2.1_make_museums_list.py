'''  Make a list of the museums and their types. '''

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2017 Black Radley Limited."

import io
from tinydb import TinyDB, Query
import helpers_list

def make_museum_list():
    ''' Create a list of all the museums in the wikipedia pages '''
    j = 0 # Counter for all the museums in England
    for county in COUNTIES_ENGLAND_CEREMONIAL:
        print '\n---'
        wikipedia_file_name = '../download/List_of_museums_' + county + '.htm'
        print 'Source: ' + wikipedia_file_name
        wikipedia_file_path = helpers_list.get_canonical_path_for(wikipedia_file_name)
        with io.open(wikipedia_file_path, 'r', encoding='utf-8') as wikipedia_file:
            wikipedia_page = wikipedia_file.read()
            museums_list = helpers_list.get_museums_list(wikipedia_page)
            for row in museums_list:
                j += 1 # counter for displaying total number of museums
                name = row['name']
                link = row['wikipedia_link']
                museum_type = row['type']
                classified_type = helpers_list.classify_type(museum_type)
                DATA_BASE.insert({'name': name, 'county': county,
                                  'classified_type': classified_type, 'link': link})
            print '\nCumulative total: {}'.format(j)


COUNTIES_ENGLAND_CEREMONIAL = helpers_list.get_counties_england_ceremonial()
DATA_BASE = TinyDB(helpers_list.get_canonical_path_for('./data/museums.json'))
# DATA_BASE.purge()
# make_museum_list()
MUSEUMS = DATA_BASE.search(Query().name == '')

print 'Total number of museums ' + len(DATA_BASE)

# The Arts Council says there are 1,600 
# http://webarchive.nationalarchives.gov.uk/20160204101926/http://www.artscouncil.org.uk/media/uploads/pdf/a_review_of_research.pdf
#   
