import urllib2, base64
import json

#This script gets all project names

#Put your API Key here
key = ""
#Put your url here minus the page number
url = "https://asas.teamwork.com/projects.json"

pagenumber = 0
tempjson = ""

#while start == 1
#pagenumber will increment at the end if a json result is found.
request = urllib2.Request(url.format())
request.add_header("Authorization", "BASIC " + base64.b64encode(key + ":xxx"))

response = urllib2.urlopen(request)
data = response.read()

#Checks if maximum page reached.
projnames = json.loads(data)
#print projnames['projects'][0]['name']

d = {}

for i in range (0, len(projnames['projects'])):
    d[projnames['projects'][i]['id']]= projnames['projects'][i]['name']
    #print projnames['projects'][i]['name']

#for i in range (0, len(projnames['projects'])):
    #print projnames['projects'][i]['id']
for key in d:
    #print key+",",
    print key, d[key]
