from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import requests
import json

bot = Bot(token='1515870254:AAETBNnrxjzwJT7K1E0eZVyNfZgfbl3lcPM')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nИспользуй команду /weather")


@dp.message_handler(commands=['weather'])
async def process_help_command(message: types.Message):
    await message.reply("Введи город")

@dp.message_handler()
async def weather(msg: types.Message):
	city = msg.text
	req = requests.get("http://api.openweathermap.org/data/2.5/weather",
	params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': '2fb5ab71084bea6a366d8b75837ae5cf'})
	data = req.json()
	if data:
		data_weather = []
		description = data['weather'][0]['description']
		temp = round(data['main']['temp'])
		speed = round(data['wind']['speed'])
		city = data['name']
		
	await bot.send_message(msg.from_user.id, "В городе " + city + " сейчас "+ description + "\nТемпература: " + str(temp) + " градус " + "\nСкорость ветра: " + str(speed) + " м/с")

if __name__ == '__main__':
	executor.start_polling(dp)