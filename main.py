import requests

URL = "http://api.weatherapi.com/v1/forecast.json"


dates = ['2023-04-17', '2023-04-18', '2023-04-19']
temps = {}

for date in dates:
    PARAMS = {'key': '0d2766c87394413582d145055231804', 'q': 'Paris', 'days': 3, 'dt': date}
    r = requests.get(url = URL, params = PARAMS)

    data = r.json()

    temps[data.get('forecast').get('forecastday')[0].get('date')] = (data.get('forecast').get('forecastday')[0].get('day').get('mintemp_f'), data.get('forecast').get('forecastday')[0].get('day').get('maxtemp_f'))

print(temps)