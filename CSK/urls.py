from django.urls import path
from . import views

app_name= "CSK"

urlpatterns=[
  path('teams',views.rile, name='index'),
]