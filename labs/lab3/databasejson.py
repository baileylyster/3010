#!/usr/bin/env python3
import sqlite3
from urllib.request import *
from urllib.parse import *
import json

dbconnect = sqlite3.connect("/home/pi/Documents/lab3/mydatabase.db")

cursor = dbconnect.cursor()

url = 'http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa'

webData = urlopen(url)
results = webData.read().decode('utf-8')
 # results is a JSON string
webData.close()
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API
data = json.loads(results)
# Print the results
current = data["main"]
degreeSym = chr(176)

sql = "INSERT INTO tblWeather (Temperature, Humidity, Pressure, Wind) values("+ str(current["temp"]) +", "+ str(current["humidity"]) + ", "+ str(current["pressure"]) + ", "+ str(data["wind"]["speed"]) +");"

cursor.execute(sql)
dbconnect.commit()

print ("Wind : %d" % data["wind"]["speed"])
