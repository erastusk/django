from django.urls import path
from . import views

app_name = 'userprofile'



urlpatterns = [    
    path('<int:id>', views.profile, name="profile"),
    path('add_city', views.profile_add_city, name="add_city"),
    path('del_city', views.profile_del_city, name="del_city")
]