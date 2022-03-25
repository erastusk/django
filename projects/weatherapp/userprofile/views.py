from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.middleware.csrf import get_token
from django.contrib.auth import login, logout, user_logged_in, user_logged_out
from .models import Profile_cities as db
from django.contrib import messages
from django.contrib.auth.models import User
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid=abf5cde6ff725334c4c2dab475a4ba51"

def profile(request, id):    
    profile_cities_list = db.objects.filter(user_id=id)     
    profile_cities = [city for city in profile_cities_list]
    if profile_cities:         
        cities = get_weather(profile_cities)  
        return render(request, 'userprofile/profile.html', {'cities' : cities})
    return render(request, 'userprofile/profile.html', {'cities' : ""})

def profile_add_city (request):    
    if request.method == 'POST' and request.POST.get('city'):        
        resp_owm =  requests.get(url.format(city_name=request.POST.get('city'))).json()
        user = request.user         
        
        if resp_owm['cod'] == 200:
            city = db.objects.filter(city=request.POST.get('city'),user=user)
            if city:  
                return redirect('userprofile:profile', id=user.id)
            else:
                new_city = db(city=request.POST.get('city'),user=user)
                new_city.save()
                return redirect('userprofile:profile',  id=user.id)
        else:           
          return redirect('userprofile:profile',  id=user.id)
    return redirect('userprofile:profile',  id=user.id)
    
def profile_del_city (request):    
    if request.method == 'POST' and request.POST.get('close_city'): 
        user = request.user         
        del_city = db.objects.filter(user=user, city__icontains=request.POST.get('close_city'))         
        if del_city:            
            del_city.delete()       
        return redirect('userprofile:profile',  id=user.id)   

    return redirect('userprofile:profile',  id=user.id)


def get_weather (cities):    
    profile_ui_cities =  []
    for city in cities:        
        resp_owm =  requests.get(url.format(city_name=city.city)).json()
        city = {
        'city' : resp_owm['name'],
        'temperature' : resp_owm['main']['temp'],
        'high' : resp_owm['main']['temp_max'],
        'low' : resp_owm['main']['temp_min'],
        'description' : resp_owm['weather'][0]['description'],
        'icon' :resp_owm['weather'][0]['icon'],
        'country_flag': resp_owm['sys']['country'].lower(),
        'country': resp_owm['sys']['country']}
        profile_ui_cities.append(city)
    return profile_ui_cities     
