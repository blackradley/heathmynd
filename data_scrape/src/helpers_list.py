""" Helpers for handling lists and wiki text 

All done mainly using regex. """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."


from bs4 import BeautifulSoup
import re # for regular expressions
import string # for string handling like 'split'

def get_ceremonial_counties_of_england():
    """ Return a list of the ceremonial counties of England """
    ceremonial_counties_of_england = []
    with open('./data/ceremonial_counties_of_england.txt') as file_of_counties:
        ceremonial_counties_of_england = file_of_counties.read().splitlines()
    return ceremonial_counties_of_england

def get_museum_type_column(the_page):
    # Get the column number of the column which contains the museum type
    soup = BeautifulSoup(the_page, "lxml")
    table = soup.find("table", {"class" : "wikitable sortable"})
    rows = table.findAll('tr')
    header = rows[0]
    


#mw-content-text > table.wikitable.sortable > tbody > tr:nth-child(1) > th:nth-child(4)

    # First find the beginning of the table '{| class="wikitable sortable"' 
    table_header_begin = re.search('\{\| class=&quot;wikitable sortable&quot;', the_page)
    
    # Then count the number of '!| ' until you get to '!| Type' 
    # This tells you what number the type column is
    table_header_end = re.search('\!\| Type', the_page)
    table_header_string = the_page[table_header_begin.end(): table_header_end.end()]
    columns = re.findall('(\!\||\!class=&quot;unsortable&quot;\|)', table_header_string)
    return len(columns)

def get_museums_list(the_page):
    # Get a list of the links to the museums in the table
    
    # Find the museum links '|- <newline?> | [[Bedford Museum & Art Gallery]]'
    museums = re.finditer('(?<=\|-\s[!|\|]\s\[\[)(?:[^|\]]*\|)?([^\]]+)(?=\]\])', the_page)
    # use ?<= and ?= to gobble up the shit at either end, unfortunately the lookbehind (?<=)
    # has to be of fixed length, so it requires the precise amount of white space.  This
    # will probably turn out to be brittle.
    links_and_names = [] # an array to return
    for museum in museums:
        # Sometimes the link and the name of the link are separated [[The Link|The Name of The Link]]
        link_and_name = string.split(museum.group(), '|')
        link = link_and_name[0] # The first part is the link, the bit I want
        name = link # If there is only a link it is also the name
        link = link.replace('&amp;', '&').replace(' ', '_') # make the link like a link
        if len(link_and_name) > 1:
            name = link_and_name[1]
        links_and_names.append([name, link])
    return links_and_names

def get_museum_types(the_page, type_column):
    # Get a list of the museum types
    
    # Find the museum links '|- <newline?> | [[Bedford Museum & Art Gallery]]'
    museums = re.finditer('(?<=\|-\s\|\s\[\[)(?:[^|\]]*\|)?([^\]]+)(?=\]\])', the_page)
    types = []
    for museum in museums:
    # 4. From each museum link count on the number of '||' you got in step 2
    # an get the type of the museum.  But first you have to get the data row
    # and split it.
        row_start = museum.start()
        row_end =  museum.start() + re.search('(\|-\s+)|(\|}\s+)', the_page[museum.start():]).end() # |- or \}
        row = the_page[row_start:row_end]
        cells = string.split(row, '||')
        type = cells[type_column - 1] # Get the cell with the type information in
        type = string.strip(type) # Remove the white space from front and back
        # For Somerset the type is also a link [[Art museum|Art]], the first bit is the link and the
        # second be is the type.
        if '|' in type:
            type = string.split(type, '|')[1].replace('[', '').replace(']', '')
        types.append(type)
    return types

def classify_type(type):
    '''It seems logical to assume that Iain's data is inconsistent, so I 
    trimmed of the first 5 characters and converted them to upper case.
    This also allows me to merge a few categories.'''
    type = type[:5].upper()
    if type == 'AGRIC': classifed_type = 'Local'
    elif type == 'AMUSE': classifed_type = 'Other'
    elif type == 'ARCHA': classifed_type = 'Historic'
    elif type == 'ART': classifed_type = 'Arts'
    elif type == 'AUTOM': classifed_type = 'Transport'
    elif type == 'AVIAT': classifed_type = 'Transport'
    elif type == 'BIOGR': classifed_type = 'Local'
    elif type == 'ENVIR': classifed_type = 'Local'
    elif type == 'FASHI': classifed_type = 'Arts'
    elif type == 'HISTO': classifed_type = 'Historic'
    elif type == 'INDUS': classifed_type = 'Industrial'
    elif type == 'LAW E': classifed_type = 'Local'
    elif type == 'LIVIN': classifed_type = 'Local'
    elif type == 'LOCAL': classifed_type = 'Local'
    elif type == 'MARIT': classifed_type = 'Transport'
    elif type == 'MEDIA': classifed_type = 'Arts'
    elif type == 'MEDIC': classifed_type = 'Other'
    elif type == 'MILIT': classifed_type = 'Other'
    elif type == 'MILL': classifed_type = 'Industrial'
    elif type == 'MININ': classifed_type = 'Industrial'
    elif type == 'MULTI': classifed_type = 'Multiple'
    elif type == 'MUSIC': classifed_type = 'Other'
    elif type == 'NATUR': classifed_type = 'Other'
    elif type == 'OPEN ': classifed_type = 'Other'
    elif type == 'PHILA': classifed_type = 'Other'
    elif type == 'PHOTO': classifed_type = 'Arts'
    elif type == 'PRISO': classifed_type = 'Local'
    elif type == 'RAILW': classifed_type = 'Transport'
    elif type == 'RELIG': classifed_type = 'Other'
    elif type == 'RURAL': classifed_type = 'Other'
    elif type == 'SCIEN': classifed_type = 'Other'
    elif type == 'SPORT': classifed_type = 'Other'
    elif type == 'TECHN': classifed_type = 'Other'
    elif type == 'TEXTI': classifed_type = 'Arts'
    elif type == 'TOY': classifed_type = 'Arts'
    elif type == 'TRANS': classifed_type = 'Transport'
    else: classifed_type = 'Other'
    return classifed_type

def iconize_type(classified_type):
    classified_type = classified_type[:5].upper()
    # http://www.google.com/fusiontables/DataSource?dsrcid=308519
    types_iconization_table = {
        'ARTS': 'small_blue',
        'HISTO': 'small_green',
        'INDUS': 'measle_turquoise',
        'LOCAL': 'small_purple',
        'MULTI': 'small_red',
        'OTHER': 'measle_white',
        'TRANS': 'small_yellow',
        }
    return types_iconization_table.get(classified_type)

 