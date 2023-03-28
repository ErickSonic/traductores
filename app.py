
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
#from flask_cors import CORS
from datetime import datetime, timedelta
#import json
import random

app = Flask(__name__)

#CORS(app, resources={r"/*": {"origins": "*"}})


global raspberry
raspberry = [
    {'tiempo': (datetime.now()+timedelta(seconds=0)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
    {'tiempo': (datetime.now()+timedelta(seconds=1)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
    {'tiempo': (datetime.now()+timedelta(seconds=2)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
    {'tiempo': (datetime.now()+timedelta(seconds=3)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)},
    {'tiempo': (datetime.now()+timedelta(seconds=4)).strftime("%H:%M:%S"), 'temperatura': round(random.uniform(-10,50),2), 'humedad': round(random.uniform(-10,50),2), 'humo': round(random.uniform(-10,50),2), 'luz': round(random.uniform(-10,50),2)}
]

global show
show = True

if not show:
    raspberry = []

@app.route('/',methods = ['GET','PUT'])
def hello_world():
    if request.method == 'GET':
        return jsonify(raspberry)
    if request.method == 'PUT':
        showState = request.json['show']
        global show
        if showState:
            show = True
            return "Solicitud correcta. Status de Show cambiado a on"
        else:
            show = False
            return "Solicitud correcta. Status de Show cambiado a off"

@app.route('/raspberry/features', methods = ['GET'])
def raspberryFeatures():
    return jsonify(raspberry)

@app.route('/raspberry/features/temperatura', methods = ['GET'])
def temperaturas():
    subTiempo = [sub['tiempo'] for sub in raspberry]
    subTemperatura = [sub['temperatura'] for sub in raspberry]

    temperaturas = []
    for i in range(len(subTemperatura)):
        temperaturas.append({
            'tiempo': subTiempo[i],
            'temperatura': subTemperatura[i]
        })
    return jsonify(temperaturas)

@app.route('/raspberry/features/humedad', methods = ['GET'])
def humedades():
    subTiempo = [sub['tiempo'] for sub in raspberry]
    subHumedad = [sub['humedad'] for sub in raspberry]

    humedad = []
    for i in range(len(subHumedad)):
        humedad.append({
            'tiempo': subTiempo[i],
            'humedad': subHumedad[i]
        })
    return jsonify(humedad)

@app.route('/raspberry/features/humo', methods = ['GET'])
def humos():
    subTiempo = [sub['tiempo'] for sub in raspberry]
    subHumo = [sub['humo'] for sub in raspberry]

    humo = []
    for i in range(len(subHumo)):
        humo.append({
            'tiempo': subTiempo[i],
            'humo': subHumo[i]
        })
    return jsonify(humo)

@app.route('/raspberry/features/luz', methods = ['GET'])
def luces():
    subTiempo = [sub['tiempo'] for sub in raspberry]
    subLuz = [sub['luz'] for sub in raspberry]

    luz = []
    for i in range(len(subLuz)):
        luz.append({
            'tiempo': subTiempo[i],
            'luz': subLuz[i]
        })
    return jsonify(luz)
