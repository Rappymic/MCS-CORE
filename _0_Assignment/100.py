import requests

API_KEY = 'db60150dfcff48a3808d256ea215ca8f'
location = 'lat=12.972442&lon=77.580643'
url = f'https://api.weatherbit.io/v2.0/current?{location}&key={API_KEY}&include=minutely'

DATA = requests.get(url)

print(DATA.text)