#! /usr/bin/python
import PTVfactory as P
import urllib as url
import json

googleKey = 'AIzaSyDejfQWInSUrLPFX8iTFQ0fBm62RdKPLNo'
baseurl = "http://timetableapi.ptv.vic.gov.au"
key = '29246674-a96c-11e3-8bed-0263a9d0b8a0'
devid = 1000050
test = P.Trans(googleKey, key, devid)

#trainlines - number of train stations
trainlinesurl = test.delegator('linesByMode',[0])
trainlines = json.load(url.urlopen(trainlinesurl))
suburb = dict()
stops = set()
lineid = set()


for i in trainlines:
	lineid.add(i['line_id'])

for i in trainlines:
	lineid = i['line_id']
	stopslineurl = test.delegator('stopsOnLine',[0,lineid])
	stopsline = json.load(url.urlopen(stopslineurl))
	for k in stopsline:
		suburb[k['suburb']] = 0
		stops.add(k['location_name'])

#how many lines for each stop?
stopsuburb = dict()
linestops = dict()
for i in trainlines:
	lineid = i['line_id']
	stopslineurl = test.delegator('stopsOnLine',[0,lineid])
	stopsline = json.load(url.urlopen(stopslineurl))
	stops2 = []
	for k in stopsline:
		stops2.append(k['location_name'])
		stopsuburb[k['location_name']] = k['suburb']
	linestops[lineid] = stops2

stoplines = dict()
for i in stops:
	for j in linestops:
		if i in linestops[j]:
			if stoplines.has_key(i):
				temp = stoplines[i][0]
				stoplines[i] = ([temp[0] + 1],stopsuburb[i])
			else:
				stoplines[i] = ([1],stopsuburb[i])


#sorted(suburb)
#stops per suburb
suburbs = dict()


for i in stoplines:
	suburb = str(stoplines[i][1])
	suburbs[suburb] = [0,0]

for i in stoplines:
	suburb = str(stoplines[i][1])
	if suburbs.has_key(stoplines[i][1]):
		suburbs[suburb][0] = suburbs[suburb][0] + 1
		suburbs[suburb][1] = stoplines[i][0][0]

file = open('trainstationdata.csv','w')
file.writelines('suburb, num_stops, num_lines')
for i in suburbs:
	file.writelines(i + "," + str(suburbs[i][0]) + "," + str(suburbs[i][1]) + "\n")


file.close()























for i in trainlines:
	lineid = i['line_id']
	stopslineurl = test.delegator('stopsOnLine',[0,lineid])
	stopsline = j.load(url.urlopen(stopslineurl))
	for k in stopsline:
		subname = k['suburb']
		if subname in suburb.keys() and k['location_name'] in stops:
			suburb[subname] += 1
			stops.remove(k['location_name'])

#tramlines - yes/no?
tramlinesurl = test.delegator('linesByMode',[1])
tramlines = j.load(url.urlopen(tramlinesurl))
suburb_2 = dict()

for i in tramlines:
	lineid = i['line_id']
	stopslineurl = test.delegator('stopsOnLine',[1,lineid])
	stopsline = j.load(url.urlopen(stopslineurl))
	for k in stopsline:
		suburb_2[k['suburb']] = 1


#sorted(suburb)

for i in tramlines:
	lineid = i['line_id']
	stopslineurl = test.delegator('stopsOnLine',[1,lineid])
	stopsline = j.load(url.urlopen(stopslineurl))
	for k in stopsline:
		subname = k['suburb']
		if subname in suburb_2.keys() and k['stop_id'] in stops_2:
			suburb_2[subname] += 1
			stops_2.remove(k['stop_id'])


#number of bus lines
buslinesurl = test.delegator('linesByMode',[2])
buslines = j.load(url.urlopen(buslinesurl))
suburb_3 = dict()


for i in buslines:
	lineid = i['line_id']
	stopslineurl = test.delegator('stopsOnLine',[2,lineid])
	stopsline = j.load(url.urlopen(stopslineurl))


weighted - bus, tram, train
