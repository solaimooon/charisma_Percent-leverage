from django.shortcuts import render
from .models import fund as mfund, Financial_data
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
from .tasks import scraping
from django.db import connection
from jdatetime import date as jdate
 


def Comparision_live_view(request):
    if not mfund.objects.exists():
        scraping.delay()
        print("داده داشت و اجرا نشد")
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def Comparision_history_chart_view(request):
    all_fund = mfund.objects.all()
    fund_data_dic = {}
    for fund in all_fund:
        # Convert dates to the desired format (e.g., YYYY-MM-DD)
        dates = list(Financial_data.objects.filter(fund=fund).values_list('date', flat=True))
        formatted_dates = [date.strftime('%Y-%m-%d') for date in dates]

        # Convert Leverage_percentage values from Decimal to float
        leverages = [
            float(leverage) for leverage in
            Financial_data.objects.filter(fund=fund).values_list('Leverage_percentage', flat=True)
        ]

        fund_data_dic[fund.name] = {
            'dates': formatted_dates,  # Dates as strings
            'leverages': leverages,  # Leverages as floats
        }

    context = {
        'fund_data': fund_data_dic  # Pass data to the template
    }
    print(context)
    return render(request, 'history.html', context)



def historycal_table(request):
    query = """
    SELECT 
        t1.date,
        t1.Leverage_percentage AS Leverage_percentage_1,
        t2.Leverage_percentage AS Leverage_percentage_2,
        t3.Leverage_percentage AS Leverage_percentage_3,
        t4.Leverage_percentage AS Leverage_percentage_4,
        t5.Leverage_percentage AS Leverage_percentage_5,
        t6.Leverage_percentage AS Leverage_percentage_6,
        t7.Leverage_percentage AS Leverage_percentage_7
    FROM 
        (SELECT date, Leverage_percentage FROM comparision_leveraged_financial_data WHERE fund_id = 7) t1
    LEFT JOIN 
        (SELECT date, Leverage_percentage FROM comparision_leveraged_financial_data WHERE fund_id = 8) t2 
        ON t1.date = t2.date
    LEFT JOIN 
        (SELECT date, Leverage_percentage FROM comparision_leveraged_financial_data WHERE fund_id = 9) t3 
        ON t1.date = t3.date
    LEFT JOIN 
        (SELECT date, Leverage_percentage FROM comparision_leveraged_financial_data WHERE fund_id = 10) t4 
        ON t1.date = t4.date
    LEFT JOIN 
        (SELECT date, Leverage_percentage FROM comparision_leveraged_financial_data WHERE fund_id = 11) t5 
        ON t1.date = t5.date
    LEFT JOIN 
        (SELECT date, Leverage_percentage FROM comparision_leveraged_financial_data WHERE fund_id = 12) t6 
        ON t1.date = t6.date
    LEFT JOIN 
        (SELECT date, Leverage_percentage FROM comparision_leveraged_financial_data WHERE fund_id = 13) t7 
        ON t1.date = t7.date
    ORDER BY 
        t1.date DESC;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # conver date to jalali
    for row in data:
        row['date'] = jdate.fromgregorian(date=row['date']).strftime('%Y/%m/%d')

    return render(request, 'table.html', {"data": data})




