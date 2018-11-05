import re # for regular expressions
import urllib # for url encoding
import urllib2 # for getting the gear from Wikipedia
from fusiontables.ftclient import *
from fusiontables.clientlogin import ClientLogin
from fusiontables.sqlbuilder import SQL

# Get a list of museums in England that have museums 
url = 'http://en.wikipedia.org/wiki/Special:Export/List_of_museums_in_England'

# to use the Wikipedia interface you must supply a User-Agent header.  The 
# policy asks for a description (http://meta.wikimedia.org/wiki/User-Agent_policy).
# If you use the browser's User-Agent header the script will probably be assumed
# to be malicious, and the IP will be blocked.   
user_agent = 'SWMuseumsMapping (+http://www.blackradley.com/contact-us/)'
headers = { 'User-Agent' : user_agent }
data = None

request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
the_page = response.read()

# Get all the museums in in England
museums = re.findall('\*\[\[(?:[^|\]]*\|)?([^\]]+)\]\],', the_page) # match *[[Bedford Museum & Art Gallery]],
del museums[10:] # reduce list for debugging purposes
print museums
print 'There are ' + str(len(museums)) + ' museums'


fileObj = open('museums.csv',"w")

'''    
{{coord|latitude|longitude|coordinate parameters|template parameters}}
{{coord|dd|N/S|dd|E/W|coordinate parameters|template parameters}}
{{coord|dd|mm|N/S|dd|mm|E/W|coordinate parameters|template parameters}}
{{coord|dd|mm|ss|N/S|dd|mm|ss|E/W|coordinate parameters|template parameters}}
'''
for museum in museums:
    url =  'http://en.wikipedia.org/wiki/Special:Export/' + str(museum).replace('&amp;', '&').replace(' ', '_')
    print url

    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    the_page = response.read()
    coord_string = re.findall('\{\{coord(?:[^|\]]*\|)?([^\]]+)\}\}', the_page) 

    data_row = "'" + museum + "', " + str(coord_string)
    print (data_row)
    fileObj.write(data_row + '\n')

fileObj.close()


raw_input("Press ENTER to exit")