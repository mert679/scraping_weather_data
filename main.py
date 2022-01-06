from bs4 import BeautifulSoup

import requests
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YcWJPCBBzIU") 

soup = BeautifulSoup(page.content,"html.parser")

seven_day_div = soup.find(id="seven-day-forecast")

forecast_items = seven_day_div.find_all(class_="tombstone-container")

# def printWeatherInfo(item):
#   period = item.find(class_="period-name").get_text()
#   shorDesc = item.find(class_="short-desc").get_text()
#   temp = item.find(class_="temp").get_text()
#   print(period)
#   print(shorDesc)
#   print(temp)

periods = []
description = []
temps = []

for forecast in forecast_items:
  #printWeatherInfo(forecast)
  period = forecast.find(class_="period-name").get_text()
  periods.append(period)

  shorDesc = forecast.find(class_="short-desc").get_text()
  description.append(shorDesc)

  temp = forecast.find(class_="temp").get_text()
  temps.append(temp)



weatherTable = pd.DataFrame(
  {
    "period":periods ,
    "short_desc": description,
    "Temp": temps
  }
)
print(weatherTable)
