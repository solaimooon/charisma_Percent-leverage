from django.urls import path,include
from .view import *
urlpatterns = [
    path("live/",Comparision_api_live_view.as_view()),
    #path("historycal_chart/",Comparision_history_chart_view,),

]