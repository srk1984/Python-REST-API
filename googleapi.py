import requests
import json
import  os
from html.parser import HTMLParser
from bs4 import BeautifulSoup

#google directions developer api_key
api_key = ''  

url = 'https://maps.googleapis.com/maps/api/directions/json&'
print("\n\n\t\t\t DISPLAYS DISTANCE AND ROUTE BETWEEN TWO PLACES")
print("\t\t\t-------------------------------------------------")
source=input("Enter the Origin  :   ")
destination = input("Enter the destination  :  ")
r=requests.get("https://maps.googleapis.com/maps/api/directions/json?"+"&origin="+source+"&destination="+destination+"&key="+api_key)

directions = json.loads(r.text)



if(directions['status'] != "OK"):
   print("Please Enter Valid Origin and Distance")
   quit()

f=open("text.txt",'w',encoding="utf-8")
f.write(r.text)
f.close()
routes=directions['routes']
legs=routes[0]['legs']

print("\n\nOrigin : ",legs[0]['start_address'])
print("\nDestination : ",legs[0]['end_address'])
print("\nDistance :",legs[0]['distance']['text'])
print("\nDuration : ",legs[0]['duration']['text'])
steps = legs[0]['steps']
print("\n\n\t\t\t DIRECTIONS ")
print("\t\t-------------------------")
print("\n")
for i in range (len(steps)):
    data=str(steps[i]['html_instructions'])
    soup = BeautifulSoup(data,features="html5lib")
    print(soup.get_text())
