import requests


async def getonl(addr):
        try:
            link = 'http://api.idena.io/api/onlineidentity/' + str(addr)
            r = requests.get(link)
            results = r.json()['result']['online']
            return results
           
            
        except KeyError:
            print("Address not found")
            return KeyError
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

