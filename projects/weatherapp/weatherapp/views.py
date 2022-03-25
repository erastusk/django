from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.middleware.csrf import get_token
import requests


url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid=abf5cde6ff725334c4c2dab475a4ba51"


resp = {
  "base": "stations", 
  "clouds": {
    "all": 20
  }, 
  "cod": 200, 
  "coord": {
    "lat": 27.9475, 
    "lon": -82.4584
  }, 
  "dt": 1635203064, 
  "id": 4174757, 
  "main": {
    "feels_like": 79.83, 
    "humidity": 90, 
    "pressure": 1011, 
    "temp": 79.83, 
    "temp_max": 82.2, 
    "temp_min": 77.72
  }, 
  "name": "Tampa", 
  "sys": {
    "country": "US", 
    "id": 2005199, 
    "sunrise": 1635161779, 
    "sunset": 1635202270, 
    "type": 2
  }, 
  "timezone": -14400, 
  "visibility": 10000, 
  "weather": [
    {
      "description": "few clouds", 
      "icon": "10d", 
      "id": 801, 
      "main": "Clouds"
    }
  ], 
  "wind": {
    "deg": 270, 
    "speed": 4.61
  }
}
default_city = {
        'city' : 'Tampa',
        'temperature' : resp['main']['temp'],
        'high' : resp['main']['temp_max'],
        'low' : resp['main']['temp_min'],
        'description' : resp['weather'][0]['description'],
        'icon' :resp['weather'][0]['icon'],
        'country': resp['sys']['country']
    }

def home(request):     
    csrf_token = get_token(request)    
    if request.method == 'POST':              
        resp_owm =  requests.get(url.format(city_name=request.POST.get('city'))).json()        
        if resp_owm['cod'] == 200:
        #If city is not found cod key value type is a string, when found it's a int.
            weather = {
                'city' : resp_owm['name'],
                'temperature' : resp_owm['main']['temp'],
                'high' : resp_owm['main']['temp_max'],
                'low' : resp_owm['main']['temp_min'],
                'description' : resp_owm['weather'][0]['description'],
                'icon' :resp_owm['weather'][0]['icon'],
                'country_flag': resp_owm['sys']['country'].lower(),
                'country': resp_owm['sys']['country']}
            return render(request, 'home.html', {'weather': weather})
        else:
            HttpResponse('City Not Found!')
    return render(request, 'home.html', {'weather':default_city})   
   