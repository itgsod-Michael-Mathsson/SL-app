# -*- coding: utf-8 -*-

__author__ = 'linus.johanssonholm'

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def whatevva():

    siteid='7000'

    apikey="1e8b0ded8e3447a181480239793d6b4f"
    apikey_site="5320242e592d42b2a16876e68b02631c"


    url="http://api.sl.se/api2/realtimedepartures.json?key={apikey}&siteid={siteid}&timewindow={timewindow}"


    url=url.format(apikey=apikey,siteid=siteid,timewindow=60)


    res=requests.get(url)

    busslist = [""]
    tidlist = [""]
    p = 0

    for rader in res.json()['ResponseData']['Buses']:
        Tid=rader['DisplayTime']
        Buss=rader['Destination']

        if Buss  ==  u"Fruängen" or Buss == u"Skarpnäck":
            busslist.insert(p, Buss)
            tidlist.insert(p, Tid)
            p += 1


    Buss1 = busslist[0]
    Buss2 = busslist[1]
    Buss3 = busslist[2]
    Buss4 = busslist[3]
    Buss5 = busslist[4]
    Buss6 = busslist[5]
    Buss7 = busslist[6]
    Buss8 = busslist[7]

    Tid1 = tidlist[0]
    Tid2 = tidlist[1]
    Tid3 = tidlist[2]
    Tid4 = tidlist[3]
    Tid5 = tidlist[4]
    Tid6 = tidlist[5]
    Tid7 = tidlist[6]
    Tid8 = tidlist[7]

    return render_template('index.html', Buss1=Buss1, Buss2=Buss2, Buss3=Buss3, Buss4=Buss4, Buss5=Buss5, Buss6=Buss6, Buss7=Buss7, Buss8=Buss8, Tid1=Tid1, Tid2=Tid2, Tid3=Tid3, Tid4=Tid4, Tid5=Tid5, Tid6=Tid6, Tid7=Tid7, Tid8=Tid8)

if __name__ == '__main__':
    app.run(debug=True)