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

#Choose which device you want to change.
async def choose_device():
    async with aiohttp.ClientSession() as session:
        global choice
        index = 0
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        for device in devices:
            print("{}: {}:".format(index, device.label))
            index += 1
        choice = input('Enter the Number of the Device You would like to control: ')
        choice = int(choice)
        device = devices[choice]


#Turn Light Red
async def light_red():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        device = devices[choice]     
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
        device = devices[choice]  
        await device.status.refresh()
        light_status = (device.status.values)
        if (light_status['switch'] == 'off'):
            await device.switch_on()
        if (light_status['hue'] != 10):
            await device.set_color(10, 100) #green=33, red=0 orange=10
            print('Light Set to Orange')
        else:
            pass

#Turn Light Green
async def light_green():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        device = devices[choice]     
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
        device = devices[choice]
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
    response = requests.get( url = apiUrl, headers = httpHeaders, params = quaryParams )
    json_response = response.json()
    status = json_response['status']
    print( response.status_code )
    if (response.status_code == 200):
        print('Status:' + status)
        if (status == 'active'):
            await light_green()
        elif (status == 'presenting' or status == 'DoNotDisturb'):
            await light_red()
        elif (status == 'call' or status == 'meeting'):           
            await light_orange()
        elif (status == 'inactive'):
            await light_off()
        else:
            pass
        
    # elif (response.status_code == 400 or 401):
        # token_refresh()
 
    
# #Refresh WebEx Token if Expired (received 400 or 401 error)
# def token_refresh():
    # global access_token
    # token_response = requests.post('https://webexapis.com/v1/access_token', data=data)
    # response_data = json.loads(token_response.text)
    # access_token = response_data['access_token']
    # token = open('webex_creds.py', 'w')
    # token.write('access_token = ' + "'" + access_token + "'")
    # token.close()
    # print ("Token Refreshed")

#Main coroutine - ask for device first, then get WebEx Status every 5 seconds
async def main():
    await choose_device()
    while True:
        await get_status()
        time.sleep(5)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
