# WebEx-Status-SmartThings-Integration

This code uses the pysmarthings library to integrate with the SmartThings API.

The script pulls your current WebEx Status using the /people/me API call every 5 seconds (configurable).

- If your status is Active, it changes the selected light to green
- If on a call or in a meeting, orange
- If presenting, red
- and if inactive, it turns the light off.

I have this working with my SmartThings connected Sylvania LED strip. The goal is to put it around my office door frame to let my family know when I'm in a meeting.<br>

## Instructions
The webex_creds.py file will hold your WebEx token. Insert your Token between the single quotes.
The st_creds.py file will hold your SmartThings Token between the single quotes
The refresh.py file will hold your WebEx refresh token and required info to refresh your token when it expires - this will NOT work if you are using your personal access token, which expires after 12 hours.

### SmartThings Setup:
When we first run "my_status.py" it will list your SmartThings devices in a numbered list like below:

            0:Living Room lights
            1:Bedroom Lights
            2:Office Lights
            3:Kitchen Lights
            Enter the Number of the Device You would like to control:

Once you enter the number of the device you want to use, it will start monitoring your WeEx status.

### WebEx Token Refresh
If you're using a Personal Access Token, which expires in 12 hours, you can comment out or remove the def token_refresh() function.



