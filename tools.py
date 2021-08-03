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
            now1 = int(now.strftime('%H%M'))
            lastseen1 = int(lastseen.strftime('%H%M'))
            diff = now1 - lastseen1
            print(now)
            print(lastseen)
            print(now1)
            print(lastseen1)
            print(diff)
            if int(diff) < 30:
               return False
            else:
               return True
 
        except KeyError:
            print("Address not found")
            return KeyError
