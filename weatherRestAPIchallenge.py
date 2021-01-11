# import the library
import requests
# Set the API endpoint
url = "https://www.metaweather.com/api/location/search/?query=bangalore"
# Send HTTP GET request to the weather query URL
response = requests.get(url)
#Convert the response to json
[weather_response] = response.json()
#grab the woeid value
woeid_value = weather_response["woeid"]
#send a request using the woeid value
woeid_url = "https://www.metaweather.com/api/location/" + str(woeid_value) + "/"
woeid_response = requests.get(woeid_url).json()
#grab the weather condition from the response.
weather_for_the_day = woeid_response["consolidated_weather"][0]["weather_state_name"]
print(weather_for_the_day)
