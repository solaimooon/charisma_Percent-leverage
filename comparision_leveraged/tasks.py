from __future__ import absolute_import, unicode_literals

from celery import shared_task

from django.shortcuts import render
from decimal import Decimal
import jdatetime
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .models import fund as mfund, Financial_data


@shared_task
#this function execute after connection _scraping
def scraping():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    time.sleep(7)
    driver = webdriver.Remote('http://selenium:4444/wd/hub', options=options)



    dic_of_fund_url = {
        "charisma":"https://ahrom.charismafunds.ir/Reports/FundNAVList?FromDate=1400%2F09%2F30&ToDate=1403%2F08%2F22&BasketId=0&page={}",
        "tavan_mofid": "https://tavanfund.com/Reports/FundNAVList?FromDate=1401%2F08%2F16&ToDate=1403%2F08%2F22&BasketId=0&page={}",
        "setab_agah": "https://shetabfund.ir/Reports/FundNAVList?FromDate=1402%2F03%2F17&ToDate=1403%2F08%2F22&BasketId=0&page={}",
        "jahesh_farabi": "https://jahesh.irfarabi.ir/Reports/FundNAVList?FromDate=1402%2F04%2F07&ToDate=1403%2F08%2F22&BasketId=0&page={}",
        "moj_firooze": "https://mojfund.ir/Reports/FundNAVList?FromDate=1402%2F08%2F22&ToDate=1403%2F08%2F22&BasketId=0&page={}",
        "narenj": "https://narenj.fund/Reports/FundNAVList?FromDate=1403%2F04%2F03&ToDate=1403%2F08%2F22&BasketId=0&page={}",
        "bidar": "https://ahrom.ebidar.ir/Reports/FundNAVList?FromDate=1403%2F04%2F03&ToDate=1403%2F08%2F22&BasketId=0&page={}"
    }

    for fund in dic_of_fund_url:
        mfund_object = mfund.objects.create(name=fund)
        page = 1
        print("صندوق",fund)
        while True:
            # open the web
            time.sleep(3)
            driver.get(dic_of_fund_url[fund].format(str(page)))

            # find the table 
            table = driver.find_element(By.CSS_SELECTOR, ".table.m-0")
            table_body = table.find_element(By.TAG_NAME, "tbody")
            rows = table_body.find_elements(By.TAG_NAME, "tr")

            if not rows:  
                break  

            # get data from cells
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                Financial_data_object = Financial_data(fund=mfund_object)
                date = jdatetime.datetime.strptime(cells[1].text, "%Y/%m/%d")
                Financial_data_object.date = date
                BaseUnitsTotalNetAssetValue = Decimal(cells[7].text.replace(',', ''))
                Financial_data_object.BaseUnitsTotalNetAssetValue = BaseUnitsTotalNetAssetValue
                SuperUnitsTotalNetAssetValue = Decimal(cells[6].text.replace(',', ''))
                Financial_data_object.SuperUnitsTotalNetAssetValue = SuperUnitsTotalNetAssetValue
                Financial_data_object.Leverage_percentage = ((BaseUnitsTotalNetAssetValue / SuperUnitsTotalNetAssetValue)-1) * 100
                Financial_data_object.save()
                print(date)


            
            page += 1
            print("صفحه",page)
    driver.quit()    