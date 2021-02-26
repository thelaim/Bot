# -*- coding: utf-8 -*-
import requests
import json

city = input('Введите город:')

req = requests.get("http://api.openweathermap.org/data/2.5/weather",
	params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': '2fb5ab71084bea6a366d8b75837ae5cf'})

data = req.json()
def weather():
	if data:
		w = data['weather'][0]['description']
		t = data['main']['temp']
		v = data['wind']['speed']
		city = data['name']
		print(w,t,v,city)
		return w, t, city
weather()