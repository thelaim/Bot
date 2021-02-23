# -*- coding: utf-8 -*-
import requests
import json

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Volgodonsk&appid=2fb5ab71084bea6a366d8b75837ae5cf')
data = req.json()
def weather():
	if data:
		w = data['weather'][0]['main']
		t = data['main']['temp'] - 273
		city = data['name']
		print(w,t,city)
		return w, t, city
weather()