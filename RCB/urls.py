from django.urls import path
from . import views

app_name= "RCB"

urlpatterns=[
    path('teams',views.home, name='index'),
  
]