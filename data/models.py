from google.appengine.ext.db import Model

class Story(Model):
  title = db.StringProperty()
