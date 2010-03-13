import cgi
import os

from django.utils import simplejson

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Ajax(webapp.RequestHandler):
  def get(self):

    url = None
    url_linktext = None
    template_values = {
        'title': 'Welcome',
        'url': url,
        'url_linktext': url_linktext,
        }

    path = os.path.join(os.path.dirname(__file__), '../index.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/ajax', Ajax)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
