import cgi
import logging
import os
import urllib

from data.models import *

from django.utils import simplejson

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Ajax(webapp.RequestHandler):
  def get(self):
    logging.info(self.request.query_string)
    logging.info(simplejson.dumps(self.request.query_string))
    for arg in self.request.arguments():
      logging.info(arg + ': ' + str(self.request.get_all(arg)))

    url = None
    url_linktext = None

    obj = {1:2, 'abcd': True}

    path = os.path.join(os.path.dirname(__file__), '../index.html')
    self.response.out.write(simplejson.dumps(obj))

class Test(webapp.RequestHandler):
  def get(self):
    logging.info('in Test')
    path = os.path.join(os.path.dirname(__file__), '../test.html')
    self.response.out.write(template.render(path, {}))

class ListLocations(webapp.RequestHandler):
  def get(self):
    logging.info('listing locations')
    l = Location()
    l.name='ryan'
    l.put()
    output = ''
    locations = self.locs()
    for loc in locations:
      output += loc.name
      output += '\n'
    
    self.response.out.write(output)

  def locs(self):
    locations = db.GqlQuery('select * from Location')
    return locations

class Search(webapp.RequestHandler):
  def get(self):
    encodedOptions = urllib.unquote(self.request.query_string)
    options = simplejson.loads(encodedOptions)
    minPrice = int(options['minPrice'])
    logging.info(minPrice)
    maxPrice = int(options['maxPrice'])
    logging.info(maxPrice)
 
    locations = db.GqlQuery("""select * from Location where
                             nonstrata_median_price >= :1 and
                             nonstrata_median_price <= :2 
                            """, minPrice, maxPrice)
    names = []
    for loc in locations:
      names.append(loc.name)# + ' ' + str(loc.nonstrata_median_price))
    self.response.out.write(simplejson.dumps(names))

application = webapp.WSGIApplication([('/ajax', Ajax),
                                      ('/ajaxtest', Test),
                                      ('/ajaxlocations', ListLocations),
                                      ('/ajaxSearch', Search),
                                      ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
