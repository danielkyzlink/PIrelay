import requests
import json
import time
import zarovky
import atexit

rele0 = None
rele1 = None

zarovky.myinit()

atexit.register(zarovky.cleanup)

# stazeni stranky
while (True):
    try:
        myjson = requests.get('http://py.prestcs.cz/rele.json')
        # overeni, ze dotaz probehl v poradku
        myjson.raise_for_status()
        data = json.loads(myjson.text)
    except Exception:
        print('soubor neni v poradku')
    else:        

        if rele0 != data['rele0']:
            rele0 = (data['rele0'])
            print("rele0:")
            print(rele0)
            if rele0:
                print("rele0 zapinam")
                zarovky.zapni4()
            else:
                print("rele0 vypinam")
                zarovky.vypni4()

        if rele1 != data['rele1']:
            rele1 = (data['rele1'])
            print("rele1:")
            print(rele1)
            if rele1:
                print("rele1 zapinam")
                zarovky.zapni17()
            else:
                print("rele1 vypinam")
                zarovky.vypni17()

    time.sleep(2)
