from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

import requests
from datetime import datetime

# Create your views here.
def index(request):
    # datetime.today().strftime('%Y-%m-%d')
    url = "https://apiv3.apifootball.com/?action=get_events&league_id=149&from=2022-08-18&to=2022-08-22&APIkey=9bc0a7e1c7bb74c27d66a79e523a86d3892afe9b52ff49a6c4f388afddfb7ddb"
    response = requests.get(url)
    jsonResponse = response.json() # Đây là 1 khu vực
    return render(request, 'blog/index.html', {'jsonResponse': jsonResponse})

def specific(request):
    return HttpResponse("This my specific url")

