import openweathermapy.core as ow

#create settings dictionary
api_key = "15383539ac6ad7827e835523385021b3"
settings = {"units" : "metric", "appid" : api_key}

#parsing is neat
current_weather_paris = ow.get_current("Paris", **settings)
summary = ["main.temp"]

data = current_weather_paris(*summary)
print("The current weather summary for Paris is:" + " " + str(data)) + "degrees celcius"