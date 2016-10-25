""" Get the county museum lists from wikipedia. 

Doing it this way, rather than cutting and pasting ensures that the same
encoding is used as urllib2 uses."""

import urllib2 # for getting the gear from Wikipedia

print '\nGet Wikipedia Data\n---'

ceremonial_counties_of_england = [
    'Bedfordshire',
    'Berkshire',
    'Bristol',
    'Buckinghamshire',
    'Cambridgeshire',
    'Cheshire',
    'Cornwall',
    'Cumbria',
    'Derbyshire',
    'Devon',
    'Dorset',
    'County_Durham',
    'the_East_Riding_of_Yorkshire',
    'East_Sussex',
    'Essex',
    'Gloucestershire',
    'Greater_Manchester',
    'Hampshire',
    'Herefordshire',
    'Hertfordshire',
    'the_Isle_of_Wight',
    'Kent',
    'Lancashire',
    'Leicestershire',
    'Lincolnshire',
    'Merseyside',
    'Norfolk',
    'Northamptonshire',
    'Northumberland',
    'North_Yorkshire',
    'Nottinghamshire',
    'Oxfordshire',
    'Rutland',
    'Shropshire',
    'Somerset',
    'South_Yorkshire',
    'Staffordshire',
    'Suffolk',
    'Surrey',
    'Tyne_and_Wear',
    'Warwickshire',
    'the_West_Midlands',
    'West_Sussex',
    'West_Yorkshire',
    'Wiltshire',
    'Worcestershire',
    'London'
    ]
data = None
headers = { 'User-Agent' : 'ProjectHeathMynd (+http://www.blackradley.com/contact-us/)' }

for county in ceremonial_counties_of_england:
    url = 'http://en.wikipedia.org/wiki/Special:Export/List_of_museums_in_' + county
    print url
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    content = response.read()
    file = open('../download/List_of_museums_in_' + county + '.wiki', 'wb')
    file.write(content)
    file.close()
