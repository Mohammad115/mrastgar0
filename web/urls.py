
from django.urls import path
from . import views
app_name= "web"
urlpatterns = [
     path('',views.home_list, name='list'),
    path('<slug>',views.weblink, name='detail'),
    path('m001/',views.m001,name='login'),

]
