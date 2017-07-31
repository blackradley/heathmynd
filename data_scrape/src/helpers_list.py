""" Helpers for handling lists and wiki text 

All done mainly using regex. """

__author__ = "Joe Collins"
__copyright__ = "Copyright (c) 2016 Black Radley Limited."

import os
from bs4 import BeautifulSoup

def get_counties_england_ceremonial():
    """ Return a list of the ceremonial counties of England """
    counties_england_ceremonial = []
    path_to_file_of_counties = get_canonical_path_for(r'data/counties_england_ceremonial.txt')
    with open(path_to_file_of_counties) as file_of_counties:
        counties_england_ceremonial = file_of_counties.read().splitlines()
    return counties_england_ceremonial

def get_canonical_path_for(file_path):
    """ Return the canonical path for a file so it doesn't matter where the script is running """
    this_script_dir = os.path.dirname(os.path.realpath(__file__))
    canonical_path = r'/'.join([this_script_dir, file_path])
    return canonical_path

def get_museums_list(wikipedia_page):
    """ Return the name, wikipedia link and type for all the museums on the page """
    page = BeautifulSoup(wikipedia_page, "lxml")
    table = page.find("table", {"class" : "wikitable sortable"})
    rows = table.findAll('tr')
    headers = rows[0].findAll('th')
    # Which column is the Type of museum?
    for index, header in enumerate(headers):
        if header.text == 'Type':
            break
    else:
        index = -1
    # Iterate through the rows makign a list of museums
    iter_rows = iter(rows)
    next(iter_rows) # Jump the first row which has the headers in
    list_of_museums = []
    for row in iter_rows:
        name = row.findAll('td')[0].text
        wikipedia_link = row.findAll('td')[0].find('a')
        if wikipedia_link is not None:
            wikipedia_link = wikipedia_link.get('href') # assumes the <a> has an <href>
        else:
            wikipedia_link = u''
        type = row.findAll('td')[index].text
        # Make a museum and append to the list
        museum = {}
        museum['name'] = name
        museum['wikipedia_link'] = wikipedia_link
        museum['type'] = type
        list_of_museums.append(museum)
    return list_of_museums

def classify_type(type):
    """ Reclassify the museums using Iain's classification """
    type = type[:5].upper() # because they can be a bit inconsistent on wikipedia
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
