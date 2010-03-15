import cgi
import logging
import os
import data.wrangle
from data.models import *
from google.appengine.ext.webapp import template

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class MainPage(webapp.RequestHandler):
  def get(self):

    url = None
    url_linktext = None
    template_values = {
        'title': 'Welcome',
        'url': url,
        'map': True,
        'url_linktext': url_linktext,
        }

    path = os.path.join(os.path.dirname(__file__), '../index.html')
    self.response.out.write(template.render(path, template_values))

class FaqPage(webapp.RequestHandler):
  def get(self):
    template_values = {
      'title': 'Frequently Asked Questions',
    }
    path = os.path.join(os.path.dirname(__file__), '../faq.html')
    self.response.out.write(template.render(path, template_values))

class AboutPage(webapp.RequestHandler):
  def get(self):
    template_values = {
      'title': 'About'
    }
    path = os.path.join(os.path.dirname(__file__), '../about.html')
    self.response.out.write(template.render(path, template_values))

class FirstRun(webapp.RequestHandler):
  def get(self):
    locs = db.GqlQuery('select * from Location')
    for loc in locs:
      loc.delete()
    any = False
    path = os.path.join(os.path.dirname(__file__), '../data')
    logging.info(os.getcwd())
    for loc in locs:
      any = True
      break;
    if not any:
      data.wrangle.importLocations(path)
      
  

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/faq.html', FaqPage),
                                      ('/about.html', AboutPage),
                                      ('/setup', FirstRun),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
