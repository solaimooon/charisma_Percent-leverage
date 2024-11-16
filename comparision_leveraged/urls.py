from django.urls import path,include
from .views import *
app_name='comparison'
urlpatterns = [
    path("",Comparision_live_view,name='live'),
    path("historycal_chart/",Comparision_history_chart_view,name="historycal_chart"),
    path("historycal_table/",historycal_table,name="historycal_table"),
    path('api/v1/',include('comparision_leveraged.api.v1.urls'))
]