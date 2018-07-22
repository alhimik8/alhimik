#!/env/python
# Python console script for Warframe,
# Which diplays Void Trader timers arrive/leave
# In which relay he will arrive
# and the items that he trades
# You can add new items in "items.json" file, using the same format.
# All data was get from "worldState.php"
# @alhimik8

import os
import time
import requests
import json
import pickle
from datetime import datetime

# script execution timer
start_time = time.time()
# get data from online worldstate json file
url = requests.get('http://content.warframe.com/dynamic/worldState.php')
content = url.content.decode('utf-8')
parse = json.loads(content)
# hack for windows - to read file in the same dir
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# load data from local items dictionary json file
with open(os.path.join(__location__, "items.json")) as data_file:
    items_list = json.load(data_file)
# parsing and matching items in online and local jsons
for x in (parse['VoidTraders']):
    print("Baro arrives into :", x['Node'])                 # on which relay arrives
    arrive = (int(x['Activation']['$date']['$numberLong'])) # when arrives
    current = datetime.now()                                # current time
    leave = (int(x['Expiry']['$date']['$numberLong']))     # when will leave
    time_come = (int(arrive / 1e3))
    time_now = (int(time.time()))

    # function clock with timers
    def time_block():
         date_arrive = (datetime.fromtimestamp(arrive / 1e3).strftime('%Y-%m-%d %H-%M-%S'))
         date_current = (datetime.strftime(current, '%Y-%m-%d %H-%M-%S'))
         date_leave = (datetime.fromtimestamp(leave / 1e3).strftime('%Y-%m-%d %H-%M-%S'))
         print("Current Time: ", date_current)
         print("Arrive:       ", date_arrive)
         print("Leave:        ", date_leave)

    # counter untill arrive or leave
    def tcounter(time_count):
        now = int(time.time())  # epoch seconds
        come = (int(time_count / 1e3)) - now  # some time in the past
        day_come = divmod(come, 86400)  # days
        hrs_come = divmod(day_come[1], 3600)  # hours
        min_come = divmod(hrs_come[1], 60)  # minutes
        sec_come = min_come[1]  # seconds
        return ('%d days, %d hours, %d minutes, %d seconds' % (day_come[0], hrs_come[0], min_come[0], sec_come))

    # if time when Baro comes is greater than current time -  Baro already leaved relay
    if (time_come - time_now > 0):
        # counter to Baro come
        print("Baro will arrive in:", tcounter(arrive))
        time_block()
    else:
        # counter to Baro leave
        print("Baro will leave in:", tcounter(leave))
        time_block()
        # creating list with matched items
        for m in (x['Manifest']):
            p = (m['ItemType'])
            print((items_list[p]).rjust(30) , "%s" %("Ducats:"), m['PrimePrice'],  "Credits:", m['RegularPrice'])
    # script execution time
        end = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))