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
    output = ''
    locations = self.locs()
    fmt = "%s %s %s %s %s"
    for loc in locations:
      output += fmt % (loc.name, loc.strata_median_price,
                       loc.nonstrata_median_price, loc.percentRise,
                       loc.url)
      output += '<br/>\n'
    
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
    stuff = []
    for loc in locations:
      item = {}
      item['name'] = loc.name
      item['price'] = loc.nonstrata_median_price
      item['url'] = loc.url
      stuff.append(item)
    self.response.out.write(simplejson.dumps(stuff))

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
