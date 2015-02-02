'''
Get a list of county list from the list of museums in England.

Joe Collins
24 March 2011

'''
import re # for regular expressions
import urllib2 # for getting the gear from Wikipedia

# The lists of museums in each county are references in the List of museums
# in England.  Using Special:Export ensures that we only get the Wiki text.
url = 'http://en.wikipedia.org/wiki/Special:Export/List_of_museums_in_England'

# To use the Wikipedia interface you must supply a User-Agent header.  The 
# policy asks for a description (http://meta.wikimedia.org/wiki/User-Agent_policy).
# If you use the browser's User-Agent header the script will probably be assumed
# to be malicious, and the IP will be blocked.   
user_agent = 'SWMuseumsMapping (+http://www.blackradley.com/contact-us/)'
headers = { 'User-Agent' : user_agent }
data = None

request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
the_page = response.read()

# Get the 46 counties in England
counties = re.findall('\{\{Main\|(?:[^|\]]*\|)?([^\]]+)\}\}', the_page) # {{Main|List of museums in Bedfordshire}}
# A hack to get 47 counties
london = re.findall('See also: \[\[(?:[^|\]]*\|)?([^\]]+)\]\]', the_page) # See also: [[List of museums in London]]
counties = counties + london

# Print the counties out to a data file, you can't use the csv module
# because it doesn't work in IronPython
fileObj = open('data\CountiesInEngland.csv',"w")
for county in counties:
    fileObj.write(str(county).replace('&amp;', '&').replace(' ', '_') + '\n')
    print county
fileObj.close()

print 'There are ' + str(len(counties)) + ' counties'
raw_input("Press ENTER to exit")
