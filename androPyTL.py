#!/usr/bin/env python

# Notifie des prochains bus et metros des transports publics
# lausannois a la station la plus proche de la position GPS
# fournie par Android, via Tasker
# 
# Copyleft 2013 Raphael Santos
# License GPL
# 
# V1.0 - 20.09.2013

import android
import urllib2
import haversine
import json
import sys

URL_STATIONS = "http://m.t-l.ch/ressources/reseau_markers.php"
URL_HORAIRES = "http://m.t-l.ch/ressources/reseau_horaire.php?id=STATION_ID"

def httpJSON(url):
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
  req = urllib2.Request(url, headers=hdr)
  try:
    page = urllib2.urlopen(req)
  except urllib2.HTTPError, e:
    print e.fp.read()
  return json.loads(page.read())


droid = android.Android()
try:
  me = droid.getIntent().result[u'extras'][u'%LOC'].split(',')
except:
  notif = "androPyTL - Error\n"
  notif += "GPS position missing"
  droid.notify("androPyTL", notif)
  sys.exit(1)

me = [float(me[0]), float(me[1])]

stations = httpJSON(URL_STATIONS)

n_station_idx = 0
for idx in range(len(stations)):
  stations[idx]['distance'] = haversine.distance(me, [float(stations[idx]['latitude']), float(stations[idx]['longitude'])])
  if stations[idx]['distance'] <= stations[n_station_idx]['distance']:
    n_station_idx = idx
station = stations[n_station_idx]

notif = station['name'] + ":\n"

horaires = httpJSON(URL_HORAIRES.replace('STATION_ID', station['id']))
horaires_tri = sorted(horaires, key=lambda k: k['time_sort']) 
for horaire in horaires_tri:
  notif += horaire['line'] + ">" + horaire['destination'] + ": " + horaire['time'] + "\n"

droid.notify("androPyTL", notif)
