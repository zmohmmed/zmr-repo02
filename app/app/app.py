#!/usr/bin/env python

import json
from bottle import request, response, redirect, run, get
from bottle import error
from datetime import datetime
from pytz import timezone
import pytz

# TODO hardcoded time zone, should get from browser or config map
TIMEZONE = 'US/Pacific'

date = datetime.now(tz=pytz.utc)
date = date.astimezone(timezone(TIMEZONE))
hour = int(date.strftime("%H"))

partOfDay = "morning" if 5<=hour<12 else "afternoon" if 12<=hour<17 else "evening"

@get('/hello')
def index():
    #print(request.headers.__dict__)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'msg': "Good %s!" % partOfDay})

@error(404)
def error404(error):
    response.headers['location'] = '/hello'
    response.status = 303
    return

run(host='0.0.0.0', port=8080)

