import requests
from typing import Dict
# added extra package
from pprint import pprint

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"
URL2 = "https://official-joke-api.appspot.com/random_ten"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "7bc51ff33209923edb37dd917be6efdb"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY, "units": "imperial"})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
def get_joke():
    res = requests.get(URL2)
    return res.json()

def main():
    temp = get_weather("Los Angeles")
    joke = get_joke()
    #used pprint instead to format the output
    print('Weather:')
    pprint(temp)
    print('Jokes:')
    for i in joke:
    	print(i['setup'])
    	print(i['punchline'])

if __name__ == "__main__":
    main()
