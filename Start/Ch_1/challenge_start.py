# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json
from pprint import pprint

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
# 1: How many quakes are there in total?
print(f"Total number of quakes: {data['metadata']['count']}")

# 2: How many quakes were felt by at least 100 people?
def getfelt(q):
    if q["properties"]["felt"] is None or q["properties"]["felt"] < 100:
        return False
    if q["properties"]["felt"] >= 100:
        return True
totalfelt = list(filter(getfelt, data["features"]))
print(f"Total quakes felt by at least 100 people: {len(totalfelt)}")

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getfeltint(q):
    if q["properties"]["felt"] is None:
        return 0
    return float(q["properties"]["felt"])
def getmag(q):
    if q["properties"]["mag"] is None:
        return 0
    return float(q["properties"]["mag"])
def getplace(q):
    if q["properties"]["place"] is None:
        return 0
    return q["properties"]["place"]
#ind = 100
#print(getfeltint(data["features"][ind]))
#print(getmag(data["features"][ind]))
#print(getplace(data["features"][ind]))

# how many quakes were felt by more than 500 people?
#res = list(filter(getmaxfelt, data["features"]))
res = max(data["features"], key=getfeltint)
place = res["properties"]["place"]
reports = res["properties"]["felt"]

print(f"The place felt by most people is: {place} with a total of {reports} reports!")


# 4: Print the top 10 most significant events, with the significance value of each
def getsig(q):
    if q["properties"]["sig"] is None:
        return 0
    return int(q["properties"]["sig"])

data['features'].sort(key=getsig, reverse=True)
print("The top 10 most significant events, with the significance values were:")
for i in range(0,10):
    event = data['features'][i]['properties']['title']
    sig = getsig(data['features'][i])
    print(f"   {event} , had significance value: {sig}")

