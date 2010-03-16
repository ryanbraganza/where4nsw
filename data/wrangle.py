"""wrangle.py"""

from data.models import *
import csv
import os
import re
import logging

def importLocations(path='.'):
  filename = os.path.join(path,'raw/suburb-medianhouseprice.csv')
  csvReader = csv.reader(open(filename))
  locations = []
  csvReader.next()
  for row in csvReader:
    name = row[0] 
    
    logging.info(row)
    strata = int(row[1])
    logging.info(str(strata))
    nonstrata = int(row[2])
    logging.info(str(nonstrata))
    l = Location(name=name,
        strata_median_price=strata,
        nonstrata_median_price=nonstrata)
    l.put()

