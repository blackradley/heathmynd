#!/usr/bin/python
# coding=UTF-8

import os
from google.appengine.api import mail
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
    def get(self):
        if self.request.path == '/':
            page = 'index.htm'
        else:
            page = self.request.path.strip('/')
        path = os.path.join(os.path.dirname(__file__), page)
        self.response.out.write(template.render(path, {}))

application = webapp.WSGIApplication([('/.*', MainPage),], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
