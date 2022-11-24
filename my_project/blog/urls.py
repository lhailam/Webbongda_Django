from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name = 'index'),
    path('specific',views.specific, name='specific'),
}

#https://apiv3.apifootball.com/?action=get_events&league_id=149&from=2022-08-18&to=2022-08-22&APIkey=9bc0a7e1c7bb74c27d66a79e523a86d3892afe9b52ff49a6c4f388afddfb7ddb