'''
Get the test data from wikipedia.  Doing it this way
rather than cutting and pasting ensures that the same
encoding is used as urllib2 uses.

Joe J Collins
31 March 2011
'''
import urllib2 # for getting the gear from Wikipedia

wiki_pages = [
              #'List_of_museums_in_Bristol',
              #'List_of_museums_in_Cornwall',
              #'List_of_museums_in_Dorset',
              #'List_of_museums_in_Devon',
              #'List_of_museums_in_Gloucestershire',
              #'List_of_museums_in_Somerset',
              #'List_of_museums_in_Wiltshire',
              'List_of_museums_in_Leicestershire'
             ]
data = None
headers = { 'User-Agent' : 'ProjectHopeBowdler (+http://www.blackradley.com/contact-us/)' }

for page in wiki_pages:
    url = 'http://en.wikipedia.org/wiki/Special:Export/' + page
    print url
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    content = response.read()
    file = open('../download/' + page + '.wiki', 'wb')
    file.write(content)
    file.close()
