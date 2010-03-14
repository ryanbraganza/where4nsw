import cgi
import os
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
  

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/faq.html', FaqPage),
                                      ('/about.html', AboutPage),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
