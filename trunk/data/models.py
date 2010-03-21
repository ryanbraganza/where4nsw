"""
models for where4nsw
"""
from google.appengine.ext.db import Expando
from google.appengine.ext import db

class Location(Expando):
  name = db.StringProperty()
  url = db.StringProperty()
  strata_median_price = db.IntegerProperty()
  nonstrata_median_price = db.IntegerProperty()
  percentRise = db.FloatProperty()

"""
loc = Location()
loc.name = 'abcd'
loc.strata_median_price = 2314
nonstrata_median_price = 423424

loc.put()

locs = db.GqlQuery('select * from Location');
for l in locs:
  print l
"""
