from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.mineral_list, name='home'),
    path('<pk>', views.mineral_detail, name='detail'),
    path('category/<str:filter_term>/',
         views.mineral_filter_category, name='filtered_category'),
    path('startswith/<str:filter_term>/',
         views.mineral_filter_name, name='filtered_name'),
    path('search/', views.mineral_search, name='search')
]
