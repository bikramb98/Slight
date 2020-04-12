import fitbit
from fitbit import gather_keys_oauth2 as Oauth2
import datetime
import requests 
import os

CLIENT_ID = '######'
CLIENT_SECRET = '######'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

if auth2_client is not None:
    os.system("pkill chromium")
    

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))


fit_statsHR = auth2_client.sleep(date='today') 

# READ LIGHT STATE
light_state = 1 

# print(fit_statsHR['sleep'][0]['minuteData'][0]['value']) #GETS THE SLEEP REQD VALUE
print(fit_statsHR['sleep'])

sleep_log =  open("sleep_log.txt","w") #TODO CHANGE FILENAME DYNAMICALLY WITH TIME 
sleep_log.write(str(fit_statsHR['sleep']))

# sleep_state = []
# 
# for i in range(0,50):
#     sleep_state.append(fit_statsHR['sleep'][0]['minuteData'][i]['value'])
# print(sleep_state)
# if '1' in sleep_state:
#     print("Bikram is sleeping")
#     
# if light_state == 1 and '1' in sleep_state:
#     print("Turning lights off")


