
def get_location():
    global lat, lon, exclude, place
    global weather
    import requests
    TOKEN2 = "d4bca8a678680fe4b1dc1c8f79c369f0"
    exclude = "minutely, hourly, alerts"
    CityName = input('State city name here: ')
    url2 = 'http://api.positionstack.com/v1/forward?access_key={}&query={}'.format(TOKEN2, CityName)
    res2 = requests.get(url2)
    data2 = res2.json()
    lat = data2['data'][0]['latitude']
    lon = data2['data'][0]['longitude']
    api_key = '547e4e1e7c99ee57e3ed55b51a3085a2'
    exclude = "minutely,hourly,alerts"
    url = 'https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude={}&appid={}'.format(lat, lon, exclude,
                                                                                                     api_key)
    res = requests.get(url)
    data = res.json()
    print(data)
    weather = data['daily'][0]['weather'][0]['main']
    print(weather)
