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
