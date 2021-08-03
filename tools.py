import requests
from datetime import datetime
import pytz

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

async def getmine(addr):
        canmine = ['Newbie', 'Verified', 'Human']
        try:
            link1 = 'http://api.idena.io/api/Epoch/Last'
            r1 = requests.get(link1)
            eph = r1.json()['result']['epoch']
            link = 'http://api.idena.io/api/Epoch/' + str(eph) +'/Identity/' + str(addr)
            r = requests.get(link)
            results = r.json()['result']['state']
            if results in canmine:
                return True
        except KeyError:
            print("Address not found")
            return KeyError
            
async def getonl1(addr):
        date_format = "%Y-%m-%dT%H:%M:%S."
        UTC = pytz.utc
        now = datetime.now(UTC)
        current_time = now.strftime(date_format)
        try:
            link = 'http://api.idena.io/api/onlineidentity/' + str(addr)
            r = requests.get(link)
            results = r.json()['result']['lastActivity']
            sub_str = "."
            res = results[:results.index(sub_str) + len(sub_str)]
            now  = datetime.strptime(current_time, date_format)
            lastseen  = datetime.strptime(res, date_format)
            diff = now - lastseen
            print(lastseen)
            print(now)

            print(diff)
            diff1 = datetime.strptime(str(diff), "%H:%M:%S")
            print(diff1)
            print("Time diff:",now - lastseen)
            print("Time diff in new format:",diff1)

            if diff1 < datetime.strptime("0:30:0", "%H:%M:%S"):
               return False
            else:
               return True
 
        except KeyError:
            print("Address not found")
            return KeyError
