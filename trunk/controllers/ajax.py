import cgi
import logging
import os

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

application = webapp.WSGIApplication(
                                     [('/ajax', Ajax),
                              ('/ajaxtest', Test)
                                          ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
