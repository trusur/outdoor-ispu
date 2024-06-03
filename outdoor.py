from __future__ import print_function
import sys
import time
import datetime
import requests
from requests.auth import HTTPBasicAuth
import json
import os
    
def category(value):
    if value <= 50: return "BAIK"
    elif value <= 100: return "SEDANG"
    elif value <= 200: return "TIDAK SEHAT"
    elif value <= 300: return "SANGAT TIDAK SEHAT"
    else: return "BERBAHAYA"
    
def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)
    
def bar_height(value):
    if value <= 50: return round(translate(value,0,50,0,19),0)
    elif value <= 100: return round(translate(value,51,100,20,38),0)
    elif value <= 200: return round(translate(value,101,200,39,57),0)
    elif value <= 300: return round(translate(value,201,300,58,76),0)
    else: return round(translate(value,301,500,77,96),0)
    
lastexec = ""
firsttime = True;

id_stasiun = open("config.cfg", "r").read()
api_url = "https://ispu.menlhk.go.id/api/public/outdoor"
auth_username = "outdoor"
auth_password = "qmzDaFwbqRtXx39q"

waktu = ""
pm10 = ""
pm25 = ""
so2 = ""
co = ""
o3 = ""
no2 = ""
hc = ""
  
while True:
    try:
        now = datetime.datetime.now()
        nowM = str(now.strftime("%M"))
        if(int(now.strftime("%S"))%15 == 0): print (now.strftime("%Y-%m-%d %H:%M:%S"))
        
        if (firsttime or nowM == "01" or nowM == "11" or nowM == "21" or nowM == "31" or nowM == "41" or nowM == "51") and now.strftime("%Y-%m-%d %H:%M") != lastexec :
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            
            print(api_url + " : " + id_stasiun)
            response = json.loads(requests.post(api_url, data={'id':id_stasiun}, auth=HTTPBasicAuth(auth_username, auth_password)).text)["data"]
            print(response)
            if(response["nama"] != ""):
                nowM0 = str(now.strftime("%M"))
                nowM0 = nowM0[0] + "0"
                run1 = str(response["run1"])
                run2 = str(response["run2"])
                pm10 = int(str(response["pm10"] or 0))
                pm25 = int(str(response["pm25"] or 0))
                so2 = int(str(response["so2"] or 0))
                co = int(str(response["co"] or 0))
                o3 = int(str(response["o3"] or 0))
                no2 = int(str(response["no2"] or 0))
                hc = int(str(response["hc"] or 0))
                if(pm10 > 500): pm10 = 500
                if(pm25 > 500): pm25 = 500
                if(so2 > 500): so2 = 500
                if(co > 500): co = 500
                if(o3 > 500): o3 = 500
                if(no2 > 500): no2 = 500
                if(hc > 500): hc = 500
                pm10_height = bar_height(pm10)
                pm25_height = bar_height(pm25)
                so2_height = bar_height(so2)
                co_height = bar_height(co)
                o3_height = bar_height(o3)
                no2_height = bar_height(no2)
                hc_height = bar_height(hc)
                
                mapping = [ 
                    ('{run1}', str(run1)), 
                    ('{run2}', str(run2)),
                    ('{pm10_height}', str(int(pm10_height))),
                    ('{pm25_height}', str(int(pm25_height))),
                    ('{so2_height}', str(int(so2_height))),
                    ('{co_height}', str(int(co_height))),
                    ('{o3_height}', str(int(o3_height))),
                    ('{no2_height}', str(int(no2_height))),
                    ('{hc_height}', str(int(hc_height))),
                    ]
                
                data = open("data.temp", "r").read()
                for k, v in mapping:
                    data = data.replace(k, v)
                
                print(data);
                
                data_new = open("data.txt","w+")
                data_new.write(data)
                data_new.close()
                os.startfile("OutdoorDisplay.exe")
                
            lastexec = now.strftime("%Y-%m-%d %H:%M")
            print("====================================================================================================");
            firsttime = False
        
        
    except Exception as e: 
        firsttime = True;
        print(e)
    
    time.sleep(1)
    