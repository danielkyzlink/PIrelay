import requests
import json
import time

rele0 = None
rele1 = None

# stažení stránky
while (True):
    try:            
        myjson = requests.get('http://py.prestcs.cz/rele.json')
        # ověření, že dotaz proběhl v pořádku
        myjson.raise_for_status()
        data = json.loads(myjson.text)
    except Exception:
        print('soubor není v pořádku')
    else:        

        if rele0 != data['rele0']:
            rele0 = (data['rele0'])
            print("rele0:")
            print(rele0)

        if rele1 != data['rele1']:
            rele1 = (data['rele1'])
            print("rele1:")
            print(rele1)

    time.sleep(2)