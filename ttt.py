import urllib2
import urllib
import json
import os
from flask import render_template, Flask,jsonify,make_response, Response
from datetime import datetime
os.environ['no_proxy']='*'

app = Flask(__name__)


def wpjson():
    r = urllib2.urlopen('http://192.168.10.1/test.json')
    data=json.load(r)
    return data

@app.route('/')
def index():
    data = wpjson()
    cisla = data['data']
    cisla1 = int(cisla[0])*10
    cisla2 = int(cisla[1])* 10
    cisla3 = int(cisla[2])* 10
    data['10'] = cisla1,cisla2,cisla3
    print data['datum']
    datum = float(data['datum'])
    data['datum'] = datetime.utcfromtimestamp(datum).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html',data=data)




if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
app.run(host='0.0.0.0',port = port)
