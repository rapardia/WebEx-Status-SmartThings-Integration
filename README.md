[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/rapardia/WebEx-Status-SmartThings-Integration)

# WebEx-Status-SmartThings-Integration

This code uses the pysmarthings library to integrate with the SmartThings API.

The script pulls your current WebEx Status using the /people/me API call every 5 seconds (configurable).

- If your status is Active, it changes the selected light to green
- If on a call or in a meeting, orange
- If presenting, red
- and if inactive, it turns the light off.

I have this working with my SmartThings connected Sylvania LED strip. The goal is to put it around my office door frame to let my family know when I'm in a meeting.

# Instructions:
## For my_status.py:
The webex_creds.py file will hold your WebEx token.

The st_creds.py file will hold your SmartThings Token.

The refresh.py file will hold your WebEx refresh token and required info to refresh your token when it expires - this will NOT work if you are using your personal access token, which expires after 12 hours.

For the above files: Open the file in a text editor and Insert your Token between the single quotes like below:

![webex_creds](https://user-images.githubusercontent.com/32777886/113059252-15986c80-9164-11eb-8f04-2e45cc75f6e5.PNG)


### SmartThings Setup:
When we first run "my_status.py" it will list your SmartThings devices in a numbered list like below:
![choose_device](https://user-images.githubusercontent.com/32777886/113059189-fdc0e880-9163-11eb-856b-d9abc1899778.PNG)

Once you enter the number of the device you want to use, it will start monitoring your WebEx status with the below output:
![my_status](https://user-images.githubusercontent.com/32777886/113059298-2517b580-9164-11eb-9dfa-8a767fdbe254.PNG)


### WebEx Token Refresh
If you're using an integration access token and not a Personal access token, you can un-comment the "token_refresh" module (lines 114-126) and add your refresh data (refresh key, client id and client refresh) to the data.py file as below:
![image](https://user-images.githubusercontent.com/32777886/113059745-a8d1a200-9164-11eb-858f-6a47d6f28399.png)


## For my_status_interactive.py:
This version is more user-friendly and removes the need for the credential files. The credentials are added manually at the launch of the program before device selection.
Downside of this version is having to manually enter your WebEx Personal access token and SmartThings Token every launch.
