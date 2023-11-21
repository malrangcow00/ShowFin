# from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
import requests

# Create your views here.
EXCHANGE_BASE_URL = settings.EXCHANGE_BASE_URL
EXCHANGE = settings.EXCHANGE
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
EXCHANGE_DATA = settings.EXCHANGE_DATA


@api_view(['GET'])
def exchange_info(request):
    params = {
        'authkey': EXCHANGE_API_KEY,
        'searchdate': (datetime.today() - timedelta(1)).strftime("%Y%m%d"), # default: today
        'data': EXCHANGE_DATA,
    }
    URL = EXCHANGE_BASE_URL + EXCHANGE
    response = requests.get(URL, params=params).json()

    return Response(response)
