import json as jsn
from pprint import pprint
import requests
import sys
import pandas as pd

response_codes = {200:'Success',
210:'Train doesn\'t run on the given date',
211:'Train doesn\'t have journey class specified',
220:'Flushed PNR',
221:'Invalid PNR',
230:'Date chosen is not valid for choen Parameters',
404:'Data couldn\'t be loaded/no data',
405:'Request couldn\'t go through',
501:'Account Expired',
502:'Invalid Arguments'}

api_key = <your-api-key>


def live_status(train_number, date):
	url = "https://api.railwayapi.com/v2/live/train/"+str(train_number)+"/date/"+str(date)+"/apikey/"+str(api_key)+"/"
	res = requests.get(url)
	data = res.json()
	res_code = data['response_code']
	if res_code != 200:
		print(response_codes[res_code])
		return res_code
	
	current_station = data['current_station']['name']
	current_station_code = data['current_station']['code']
	running_status = data['position']
	count=0
	for i in data['route']:
		count = count + 1
		if current_station_code == i['station']['code']:
			break;
	next_station = data['route'][count+1]['station']['name']

	print("Live Status: ", running_status)
	print("Next Station: ", next_station)
	return res_code

def seat_avail(train_number, date, source, dest, pref, quota):
	classes = {'2A':'SECOND AC','CC':'AC CHAIR CAR','2S':'SECOND SEATING','FC':'FIRST CLASS','1A':'FIRST AC','3A':'THIRD AC','3E':'THIRD AC ECONOMY','SL':'SLEEPER'}
	url = "https://api.railwayapi.com/v2/check-seat/train/"+str(train_number)+"/source/"+str(source)+"/dest/"+str(dest)+"/date/"+str(date)+"/pref/"+str(pref)+"/quota/"+str(quota)+"/apikey/"+str(api_key)+"/"
	res = requests.get(url)
	data = res.json()
	res_code = data['response_code']
	if res_code != 200:
		print(response_codes[res_code])
		return res_code

	train_name = data['train']['name']
	df = pd.DataFrame.from_dict(data['availability'],orient='columns')
	print("\n")
	print("\nTrain Number: ", data['train']['number'], "\tName: ", train_name)
	print("\tAvailability: ", pref," : ", classes[pref])
	print()
	print(df)
	return res_code

def pnr_stat(train_number, date, pnr):
	return 0

sample_url = "https://api.railwayapi.com/v2/live/train/<train number>/date/<dd-mm-yyyy>/apikey/<apikey>/"
classes = {'2A':'SECOND AC','CC':'AC CHAIR CAR','2S':'SECOND SEATING','FC':'FIRST CLASS','1A':'FIRST AC','3A':'THIRD AC','3E':'THIRD AC ECONOMY','SL':'SLEEPER'}


train_number = input("Enter the train number: ").strip()
date = input("Enter the date on which the train starts(dd-MM-yyyy): ").strip()
try:
	train_number = int(train_number)
	if train_number > 99999 :
		print("Invalid Train number")
except Exception as ex:
	print("Invalid Train Number: ", ex)


print("1. Live Status\n2. Seat Availability\n3. PNR status")
choice = input("Enter your choice: ").strip()
try:
	choice = int(choice)
except:
	print("Invalid Option. Enter an Integer")
if choice <=3 and choice >=1:
	if choice==1:
		status = live_status(train_number, date)
		if status == 200:
			print("Success..")
		else:
			print("Failure")
	if choice==2:
		source = input("Enter code of Source station: ").strip()
		dest = input("Enter code of destination station: ").strip()
		clss = pd.DataFrame.from_dict(classes, orient='index')
		print("\n\n", clss)
		pref = input("\nEnter class preference: ").strip()
		quota = input("Enter Quota: ").strip()
		status = seat_avail(train_number,date,source,dest,pref,quota)
		if status == 200:
			print("Success..")
		else:
			print("Failure")



