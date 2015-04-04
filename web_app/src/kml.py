#!/usr/bin/python
# coding=UTF-8

import urllib2
import re
from xml.dom.minidom import parseString
from google.appengine.api import mail
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp

data = None
headers = { 'User-Agent' : 'ProjectHeathMynd (+http://www.blackradley.com/contact-us/)' }

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml'
        name = self.request.get('name')
        if name == 'museum': 
            content = self.get_museums()
        else: 
            content = 'Other'
        self.response.out.write(content)
        
    def get_museums(self):
        url = 'http://www.google.com/fusiontables/exporttable?query=select+col0%2C+col1%2C+col2%2C+col6%2C+col3%2C+col4%2C+col5+from+614442+&o=kmllink&g=col3'
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        kml = response.read()
        dom = parseString(kml)
        placemark_nodes = dom.getElementsByTagName("Placemark")
        for node in placemark_nodes:
            extended_data_node = dom.getElementsByTagName("ExtendedData")[0]
            node.removeChild(extended_data_node)
            
        # Remove the blank lines and the Folder element.    
        xml = '\n'.join([s for s in dom.toxml().splitlines() if s])
        xml = xml.replace('<Folder id="Fusiontables">\n', '').replace('</Folder>\n', '')
        return xml
    
application = webapp.WSGIApplication([('/.*', MainPage),], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
