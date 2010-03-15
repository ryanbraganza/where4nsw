"""wrangle.py"""

from data.models import *
import csv
import os
import re

def importLocations(path='.'):
  filename = os.path.join(path,'raw/suburb-medianhouseprice.csv')
  csvReader = csv.reader(open(filename))
  locations = []
  csvReader.next()
  regex = re.compile('/,/')
  for row in csvReader:
    name = row[0] 
    
    strata = int('0' + regex.sub(row[1],''))
    nonstrata = int('0' + regex.sub(row[2],''))
    l = Location(name=name,
        strata_median_price=strata,
        nonstrata_median_price=nonstrata)
    l.put()

