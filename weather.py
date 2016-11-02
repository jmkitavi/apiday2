# coding=utf-8
import urllib2, urllib, json

baseurl = "https://query.yahooapis.com/v1/public/yql?"
    #baseusrl as provided in yahoo weather api doc
yql_query = "select * from weather.forecast where woeid=2345940"
    #yql(Yahoo Query Language) is query for Yahoo weather database
    #woeid is where on earth id for Nairobi = 2345940
yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result) #loading json results

#f = open("dump.json",'w')
#f.write(result)
#f.close()
weather = data['query']['results']['channel'] #formatting and outputting the data

print weather['description']

print '\t Date:' + weather['item']['condition']['date']
print '\t Temperature:' + weather['item']['condition']['temp'] + u' °F'
print '\t Weather:' + weather['item']['condition']['text']

for forecast in weather['item']['forecast']:
    print '\n\t Date:' + forecast['date']
    print '\t Temperature:' + str((int(forecast['low']) + int(forecast['high'])) / 2) + u' °F'
    print '\t Weather:' + forecast['text']
