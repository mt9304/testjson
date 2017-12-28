import urllib2, base64
import json

#Put your API Key here
key = "aaa"
#Put your url here minus the page number
url = "https://asas.teamwork.com/projects/283813/latestactivity.json?page="

pagenumber = 0
start = 1
tempjson = ""

while start == 1:
        #pagenumber will increment at the end if a json result is found. 
        request = urllib2.Request(url+str(pagenumber).format())
        request.add_header("Authorization", "BASIC " + base64.b64encode(key + ":xxx"))
         
        response = urllib2.urlopen(request)
        data = response.read()



        #Checks if maximum page reached. 
        if data != "{\"activity\":[],\"STATUS\":\"OK\"}":
                tempjson = tempjson + data
                pagenumber += 1
                print "Found Page " + str(pagenumber)
        else:
                print "No page"
                start = 0
                #break
print "Task completed"
pagenumber = 0

f = open("testfile.txt", "w")
f.write(tempjson)
f.close
