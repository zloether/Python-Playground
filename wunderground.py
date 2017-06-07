#!/usr/bin/env python
# wunderground.py

# imports
import requests, collections

# -----------------------------------------------------------------------------
# global variables
# -----------------------------------------------------------------------------
# https://www.wunderground.com/weather/api
apiKey = 'insert_wunderground_api_key_here'
apiurl = 'https://api.wunderground.com/api/'

# -----------------------------------------------------------------------------
# wunderground_current
# -----------------------------------------------------------------------------
def wunderground_current(search_term):

    target_url = apiurl + apiKey + '/conditions/q/' + search_term + '.json'
    response = requests.get(target_url)
    response_json = response.json()

    weather = collections.OrderedDict() # initialize ordereddict for response data

    weather['Observed site'] = response_json['current_observation']['observation_location']['full']
    weather['Last updated'] = response_json['current_observation']['observation_time_rfc822']
    weather['Local time'] = response_json['current_observation']['local_time_rfc822']
    weather['Time zone'] = response_json['current_observation']['local_tz_short']
    weather['Temperature'] = response_json['current_observation']['temperature_string']
    weather['Feels like'] = response_json['current_observation']['feelslike_string']
    weather['Humidity'] = response_json['current_observation']['relative_humidity']
    weather['Wind behavior'] = response_json['current_observation']['wind_string']

    return weather

# -----------------------------------------------------------------------------
# print_wunderground_current
# -----------------------------------------------------------------------------
def print_wunderground_current(input_data):
    weather = wunderground_current(input_data)

    for item in weather:
        print(str(item) + ":\t" + str(weather[item]))

# -----------------------------------------------------------------------------
# wunderground_forecast
# -----------------------------------------------------------------------------
def wunderground_forecast(search_term):

    target_url = apiurl + apiKey + '/forecast/q/' + search_term + '.json'
    response = requests.get(target_url)
    response_json = response.json()

    weather = collections.OrderedDict() # initialize ordereddict for response data

    i = 0
    while i < 4:
        weather['day' + str(i)] = response_json['forecast']['simpleforecast']['forecastday'][i]['date']['weekday']
        weather['high' + str(i)] = response_json['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit']
        weather['low' + str(i)] = response_json['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit']
        weather['sky' + str(i)] = response_json['forecast']['simpleforecast']['forecastday'][i]['conditions']
        weather['precip' + str(i)] = response_json['forecast']['simpleforecast']['forecastday'][i]['pop']
        i = i+1

    return weather

# -----------------------------------------------------------------------------
# print_wunderground_forecast
# -----------------------------------------------------------------------------
def print_wunderground_forecast(input_data):
    weather = wunderground_forecast(input_data)

    i = 0 # initialize iterator
    while i < 4:
        print(str(weather['day' + str(i)]))
        print("-------------")
        print("High:\t" + str(weather['high' + str(i)]))
        print("Low:\t" + str(weather['low' + str(i)]))
        print("Sky:\t" + str(weather['sky' + str(i)]))
        print("Pre:\t" + str(weather['precip' + str(i)]) + "%")
        print()
        i = i+1

# -----------------------------------------------------------------------------
# wunderground_forecast_text
# -----------------------------------------------------------------------------
def wunderground_forecast_text(search_term):

    target_url = apiurl + apiKey + '/forecast/q/' + search_term + '.json'
    response = requests.get(target_url)
    response_json = response.json()

    weather = collections.OrderedDict() # initialize ordereddict for response data

    i = 0
    while i < 8:
        weather['title' + str(i)] = response_json['forecast']['txt_forecast']['forecastday'][i]['title']
        weather['text' + str(i)] = response_json['forecast']['txt_forecast']['forecastday'][i]['fcttext']
        weather['precip' + str(i)] = response_json['forecast']['txt_forecast']['forecastday'][i]['pop']
        i = i+1

    return weather

# -----------------------------------------------------------------------------
# print_wunderground_forecast_text
# -----------------------------------------------------------------------------
def print_wunderground_forecast_text(input_data):
    weather = wunderground_forecast_text(input_data)

    i = 0 # initialize iterator
    while i < 8:
        print(str(weather['title' + str(i)]))
        print("----------------")
        print(str(weather['text' + str(i)]))
        print("Precipitation:\t" + str(weather['precip' + str(i)]) + "%")
        print()
        i = i+1

# -----------------------------------------------------------------------------
# print_help
# -----------------------------------------------------------------------------
def print_help():
    print("Get the the weather from Wunderground.com")
    print()
    print("Usage: wunderground.py <subcommand> <location>")
    print("subcommands: current, forecast, forecasttext")
    print("\t\"text\" also works instead of \"forecasttext\"")
    print()
    print("zip-codes work best for location, however city and state " +\
             "will usually work as long as they are enclosed in quotes " +\
             "(e.g., \"new york ny\")")
    print()
    print("Sample usage:")
    print("wunderground.py current 11419")
    print("wunderground.py forecast manhattan")
    print("wunderground.py forecasttext \"new york ny\"")
    exit()

# -----------------------------------------------------------------------------
# run it
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    from sys import argv
    try:
        script, subcommand, input_data = argv
    except:
        print_help()

    if subcommand == "current":
        print_wunderground_current(input_data)
    elif subcommand == "forecast":
        print_wunderground_forecast(input_data)
    elif subcommand == "forecasttext" or subcommand == "text":
        print_wunderground_forecast_text(input_data)
    else:
        print("Error! Unrecognized subcommand.")
        print()
        print_help()
