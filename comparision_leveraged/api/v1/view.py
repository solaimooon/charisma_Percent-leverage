from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json

# api for live section
class Comparision_api_live_view(APIView):
    # get method
    def get(self,request):
        # api url charisma
        karisma_api = "https://ahrom.charismafunds.ir/Fund/GetLeveragedNAV"
        # request to api
        karisma_response = requests.get(karisma_api)
        # convert json to dict first time
        karisma_data_str = json.loads(karisma_response.text)
        # convert json to dict second time
        karisma_data_dict = json.loads(karisma_data_str)
        # get BaseUnitsTotalNetAssetValue as float
        karisma_BaseUnitsTotalNetAssetValue = float(karisma_data_dict['BaseUnitsTotalNetAssetValue'].replace(",",""))
        print(karisma_BaseUnitsTotalNetAssetValue,"کاریزما عادی")
        #get SuperUnitsTotalNetAssetValue as float
        karisma_SuperUnitsTotalNetAssetValue = float(karisma_data_dict ['SuperUnitsTotalNetAssetValue'].replace(",",""))
        print(karisma_SuperUnitsTotalNetAssetValue, "کاریزما امتیاز")
        # calculate Leverage percentage
        result_karisma = ((karisma_BaseUnitsTotalNetAssetValue / karisma_SuperUnitsTotalNetAssetValue)-1) * 100
        # api url mofid
        mofid_api = "https://tavanfund.com/Fund/GetLeveragedNAV"
        mofid_response = requests.get(mofid_api, verify=False)
        mofid_data_str = json.loads(mofid_response.text)
        mofid_data_dict = json.loads(mofid_data_str)
        mofid_BaseUnitsTotalNetAssetValue = float(mofid_data_dict['BaseUnitsTotalNetAssetValue'].replace(",",""))
        mofid_SuperUnitsTotalNetAssetValue = float(mofid_data_dict['SuperUnitsTotalNetAssetValue'].replace(",",""))
        result_mofid = ((mofid_BaseUnitsTotalNetAssetValue / mofid_SuperUnitsTotalNetAssetValue)-1) * 100
        # api url shetab
        agah_api = "https://shetabfund.ir/Fund/GetLeveragedNAV"
        agah_response = requests.get(agah_api)
        agah_data_str = json.loads(agah_response.text)
        agah_data_dict = json.loads(agah_data_str)
        agah_BaseUnitsTotalNetAssetValue = float(agah_data_dict['BaseUnitsTotalNetAssetValue'].replace(",",""))
        agah_SuperUnitsTotalNetAssetValue = float(agah_data_dict['SuperUnitsTotalNetAssetValue'].replace(",",""))
        result_agah = ((agah_BaseUnitsTotalNetAssetValue / agah_SuperUnitsTotalNetAssetValue)-1) * 100
        # api url farabi
        farabi_api = "https://jahesh.irfarabi.ir/Fund/GetLeveragedNAV"
        farabi_response = requests.get(farabi_api)
        farabi_data_str = json.loads(farabi_response.text)
        farabi_data_dict = json.loads(farabi_data_str)
        farabi_BaseUnitsTotalNetAssetValue = float(farabi_data_dict['BaseUnitsTotalNetAssetValue'].replace(",",""))
        farabi_SuperUnitsTotalNetAssetValue = float(farabi_data_dict['SuperUnitsTotalNetAssetValue'].replace(",",""))
        result_farabi = ((farabi_BaseUnitsTotalNetAssetValue / farabi_SuperUnitsTotalNetAssetValue)-1) * 100
        # api url moj
        moj_api = "https://mojfund.ir/Fund/GetLeveragedNAV"
        moj_response = requests.get(moj_api)
        moj_data_str = json.loads(moj_response.text)
        moj_data_dict = json.loads(moj_data_str)
        moj_BaseUnitsTotalNetAssetValue = float(moj_data_dict['BaseUnitsTotalNetAssetValue'].replace(",",""))
        moj_SuperUnitsTotalNetAssetValue = float(moj_data_dict['SuperUnitsTotalNetAssetValue'].replace(",",""))
        result_moj = ((moj_BaseUnitsTotalNetAssetValue / moj_SuperUnitsTotalNetAssetValue)-1) * 100
        # narenj
        narenj_api = "https://narenj.fund/Fund/GetLeveragedNAV"
        narenj_response = requests.get(narenj_api)
        narenj_data_str = json.loads(narenj_response.text)
        narenj_data_dict = json.loads(narenj_data_str)
        narenj_BaseUnitsTotalNetAssetValue = float(narenj_data_dict['BaseUnitsTotalNetAssetValue'].replace(",",""))
        narenj_SuperUnitsTotalNetAssetValue = float(narenj_data_dict['SuperUnitsTotalNetAssetValue'].replace(",",""))
        result_narenj = ((narenj_BaseUnitsTotalNetAssetValue / narenj_SuperUnitsTotalNetAssetValue)-1) * 100
        # bidar
        bidar_api = "https://ahrom.ebidar.ir/Fund/GetLeveragedNAV"
        bidar_response = requests.get(bidar_api)
        bidar_data_str = json.loads(bidar_response.text)
        bidar_data_dict = json.loads(bidar_data_str)
        bidar_BaseUnitsTotalNetAssetValue = float(bidar_data_dict['BaseUnitsTotalNetAssetValue'].replace(",",""))
        bidar_SuperUnitsTotalNetAssetValue = float(bidar_data_dict['SuperUnitsTotalNetAssetValue'].replace(",",""))
        result_bidar=((bidar_BaseUnitsTotalNetAssetValue/bidar_SuperUnitsTotalNetAssetValue)-1)*100
        # contex
        Leverage_percentage={"karisma":result_karisma,"mofid":result_mofid,"agah":result_agah,
                             "farabi":result_farabi,"moj":result_moj,"narenj":result_narenj,
                             "bidar":result_bidar}
        return Response(Leverage_percentage,status=status.HTTP_200_OK)
