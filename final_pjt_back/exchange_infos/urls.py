from django.urls import path
from . import views

app_name = 'exchange_infos'
urlpatterns = [
    path('', views.exchange_info),
]