
import json
import requests
import time
import matplotlib.pyplot as plt

API = 'https://api.github.com/repos/mbostock/d3/stats/commit_activity'
#from the dev github website (https://developer.github.com/v3/repos/statistics/), figure out how to get last year(52wks)
#of commit data. Type in https://api.github.com/repos/mbostock/d3/stats/commit_activity (filling in "https://api.github.com"
#in the GET part, "mbostock" in the :users part, and "d3" in the :repo part

def epoch_returner(api_address): #this will pull in the weekly commit totals, find the max commit #, and the corresponding week's epoch
    r = requests.get(api_address)
    jsonoutput = r.json() #digesting the json data into a consumable format by importing the requests module and using the JSON decoder
    mylist = []
    for i in range(0, len(jsonoutput)-1): #iterate thru the JSON array and add the commit totals in our empty list
        mylist.append(jsonoutput[i]["total"])
    max_value = (max(mylist))
    max_indices = [n for n in range(len(jsonoutput)-1) if mylist[n] == max_value]
    #find the corresponding indices for the max commit total wk with list comprehension

    for x in max_indices:
        numb_of_max_wk = jsonoutput[int(x)]["week"] #with the indices number, find and return the corresponding week start date.
    return numb_of_max_wk

print(epoch_returner(API))


def convert_epoch_time(epoch_time):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time)) #stack overflow tip: how to convert epoch into a formatted string

print(convert_epoch_time(epoch_returner(API)))


def weekday_tally(api_address): #want to create a dictionary to tally up weekday commit counts
    r = requests.get(api_address)
    jsonoutput = r.json()
    mydict = {"Sunday":0, "Monday":0, "Tuesday":0, "Wednesday":0, "Thursday":0, "Friday":0, "Saturday":0} #setting intial values all at 0
    for i in range(0, len(jsonoutput)-1):
        mydict["Sunday"] = mydict["Sunday"] + jsonoutput[i]["days"][0]
        mydict["Monday"] = mydict["Monday"] + jsonoutput[i]["days"][1]
        mydict["Tuesday"] = mydict["Tuesday"] + jsonoutput[i]["days"][2]
        mydict["Wednesday"] = mydict["Wednesday"] + jsonoutput[i]["days"][3]
        mydict["Thursday"] = mydict["Thursday"] + jsonoutput[i]["days"][4]
        mydict["Friday"] = mydict["Friday"] + jsonoutput[i]["days"][5]
        mydict["Saturday"] = mydict["Saturday"] + jsonoutput[i]["days"][6]
    print(mydict) #print compiled dictionary to see
    maxval = max(mydict.values()) #find the maximum tally number

    plt.bar(range(len(mydict)), mydict.values(), align='center') #use matplotlib to create a barplot from our dictionary
    plt.xticks(range(len(mydict)), list(mydict.keys()))

    plt.show()

    topday = [k for k,v in mydict.items() if v == maxval] #use list comprehension and dict.items to return the corresponding top date.
    return topday

print(weekday_tally(API))



#code from when I was looking at indiv commits: no good because it only looked at the user's commits.

#import dateutil.parser
#import datetime
#from datetime import date
#
# def dateconverter(api_address):
#
#     r = requests.get(api_address)
#     jsonoutput = r.json()
#     #total = []
#     for i in range(0, len(jsonoutput)-1):
#         modified = (jsonoutput[i]["commit"]["author"]["date"])
#               #at this point, modified gives something like: "2015-04-06T22:28:16Z"
#         new_format = (int(modified[0:4]), int(modified[5:7]), int(modified[8:10]))
#         total = ((date.weekday(date(*new_format))))
#         return(total)
#
# print(dateconverter('https://api.github.com/repos/mbostock/d3/commits?since=2014-04-19330:00:000'))

# # here's an alternative:::::
# #
# # my_date = dateutil.parser.parse(modified)
# # is_wk_day = date.weekday(my_date)
# #
# # print(is_wk_day)
