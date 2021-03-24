import requests
import aiohttp
import asyncio
import pysmartthings
import json
import time
#import credentials for WebEx and SmartThings
from webex_creds import access_token
from st_creds import token
from refresh import data


#SmartThings

# Turn Light Red
async def light_red():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        device = devices[2]     
        await device.status.refresh()
        light_status = (device.status.values)
        if (light_status['switch'] == 'off'):
            await device.switch_on()
        if (light_status['hue'] != 0 ):
            await device.set_color(0, 100)
            print('Light Set to Red')
        else:
            pass
   
#Turn Light Orange                    
async def light_orange():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        device = devices[2]  
        await device.status.refresh()
        light_status = (device.status.values)
        if (light_status['switch'] == 'off'):
            await device.switch_on()
        if (light_status['hue'] != 10):
            await device.set_color(10, 100) #green=33, red=0 orange=10
            print('Light Set to Orange')
        else:
            pass

# Turn Light Green
async def light_green():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        device = devices[2]     
        await device.status.refresh()
        light_status = (device.status.values)
        if (light_status['switch'] == 'off'):
            await device.switch_on()
        if (light_status['hue'] != 33 ):
            await device.set_color(33, 100)
            print('Light Set to Green')
        else:
            pass

#Turn Light Off                   
async def light_off():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        device = devices[2]
        await device.status.refresh()
        status = (device.status.values ['switch'])
        if (status != 'off'):
            await device.switch_off()
            print('Light Switched Off')
        else:
            pass

#Get WebEx status
async def get_status():
    #Identify the WebEx API Call and Params
    apiUrl = 'https://webexapis.com/v1/people/me'
    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    quaryParams = { 'callingData': 'false' }
    #GET current WebEx Status
    response = requests.get( url = apiUrl, headers = httpHeaders, params = quaryParams )
    json_response = response.json()
    print( response.status_code )
    if (response.status_code == 200):
        if (json_response['status'] == 'active'):
            print('Status:' + json_response ['status'])
            await light_green()
        elif (json_response['status'] == 'presenting'):
            print('Status:' + json_response['status'])
            await light_red()
        elif (json_response['status'] == 'call', 'meeting'):
            print('Status:' + json_response['status'])
            await light_orange()
        elif (json_response['status'] == 'inactive'):
            print('Status:' + json_response['status'])
            await light_off()
        
    elif (response.status_code == 400 or 401):
        token_refresh()
 
    
#Refresh WebEx Token if Expired (recieved 400 or 401 error)
def token_refresh():
    token_response = requests.post('https://webexapis.com/v1/access_token', data=data)
    response_data = json.loads(token_response.text)
    access_token = response_data['access_token']
    token = open('creds.py', 'w')
    token.write('access_token = ' + "'" + access_token + "'")
    token.close()
    print ("Token Refreshed")

#Run main corutine and loop every 5 seconds
while True:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_status())
    time.sleep(5)
