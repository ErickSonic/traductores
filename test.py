from flask import Flask, jsonify
import random
import time
from datetime import datetime, timedelta
import json

# t = time.localtime()
# print(t.)
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# current_time1 = (now + timedelta(seconds=1)).strftime("%H:%M:%S")
# print(current_time)
# print(current_time1)

raspberry = []
jsonFile = open('raspberry.json', 'r')
raspberryJson = json.load(jsonFile)
for i in raspberryJson['raspberry']:
    raspberry.append(i)
    #print(i)
# print(raspberry)
jsonFile.close()

# print(raspberryJson['show'])
# raspberryJson['show'] = False
# print(raspberryJson['show'])

raspberryJson['raspberry'].append({
    'tiempo': '11:40:00',
    'temperatura': 5.0,
    'humedad': 30.0,
    'humo': 10.0,
    'luz': 15.0
})
raspberry.append({
    'tiempo': '11:40:00',
    'temperatura': 5.0,
    'humedad': 30.0,
    'humo': 10.0,
    'luz': 15.0
})
print(raspberryJson['raspberry'])

jsonFile = open('raspberry.json', 'w+')
jsonFile.write(json.dumps(raspberryJson))
jsonFile.close()

# raspberry = [
#     {'tiempo': (datetime.now()+timedelta(seconds=0)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
#     {'tiempo': (datetime.now()+timedelta(seconds=1)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
#     {'tiempo': (datetime.now()+timedelta(seconds=2)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
#     {'tiempo': (datetime.now()+timedelta(seconds=3)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
#     {'tiempo': (datetime.now()+timedelta(seconds=4)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)}
# ]
print('\n')
print(raspberry)
print('\n')

# res = [sub['temperatura'] for sub in raspberry]
# print(str(res))

subTiempo = [sub['tiempo'] for sub in raspberry]
subTemperatura = [sub['temperatura'] for sub in raspberry]

temperaturas = []
for i in range(len(subTemperatura)):
    temperaturas.append({
        'tiempo': subTiempo[i],
        'temperatura': subTemperatura[i]
    })

# hola = 'temperatura'
# subTemperatura = [sub[hola] for sub in raspberry]
# print(subTemperatura)
# resTi = [sub['tiempo'] for sub in raspberry]
# timeT = [dict(zip(['temperatura'],[i])) for i in resTi]
# resTe = [sub['temperatura'] for sub in raspberry]
# temperatures = [dict(zip(['temperatura'],[i])) for i in resTe]

# print(raspberry)
# print(temperaturas)

if False:
    print('hola')
elif 3<2 or 3==3:
    print('hello')