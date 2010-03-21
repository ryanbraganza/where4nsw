"""wrangle.py"""

from data.models import *
import csv
import os
import re
import logging

def getLocation(name):
  query = Location.all()
  query.filter('name =', name)
  location = query.get()
  if location == None:
    location = Location(name=name)
    location.put()
  location = query.get()
  return location

def importLocations(path='.'):
  filename = os.path.join(path,'raw/suburb-medianhouseprice.csv')
  csvReader = csv.reader(open(filename))
  csvReader.next()
  for row in csvReader:
    name = row[0] 
    logging.info(row)
    strata = int(row[1])
    logging.info(str(strata))
    nonstrata = int(row[2])
    logging.info(str(nonstrata))
    l = getLocation(name)
    l.strata_median_price=strata
    l.nonstrata_median_price=nonstrata
    l.put()

  filename = os.path.join(path,'raw/suburb-percentage_increase_2bed_house.csv')
  csvReader = csv.reader(open(filename))
  for row in csvReader:
    name = row[0]
    l = getLocation(name)
    l.percentRise = float('0'+row[1])
    l.put()

  filename = os.path.join(path,'raw/suburb-url.csv')
  csvReader = csv.reader(open(filename))
  for row in csvReader:
    name = row[0]
    l = getLocation(name)
    l.url = row[1]
    l.put()
    

