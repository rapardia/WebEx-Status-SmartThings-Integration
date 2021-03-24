# WebEx-Status-SmartThings-Integration

This code uses the pysmarthings library to integrate with the SmartThings API.

The script pulls your current WebEx Status using the /people/me API call every 5 seconds (configurable).

If your status is Active, it changes the selected light to green
If on a call or in a meeting, Orange
If presenting, red
and if inactive, it turns the light off.

I have this working with my SmartThings connected Sylvania LED strip. The goal is to put it around my office door frame to let my family know when I'm buys.

# Instructions
The webex_creds.py file will hold your WebEx token. Insert your Token between the single quotes.
The st_creds.py file will hold your SmartThings Token between the single quotes
The refresh.py file will hold your WebEx refresh token and required info to refresh your token when it expires - this will NOT work if you are using your personal access token

# SmartThings Setup:
Before we begin, we need to identify the light you want to use:
Open get_devices.py and insert your SmartThings API key between the quotes:
    # token = '12343-12334-1234123213'
Run get_devices.py, the output should look similar to this:

    12345678-12345-1234-8956-12345896fdf:Living Room lights
    12265678-12345-1569-8246-789345896fd:Bedroom Lights
    98565678-12345-1234-8956-54987896fdf:Office Lights
    
Once you identify the device you want to use, note which position it is in starting from zero. e.g. "Office Lights" would be position 2.

In my_status.py replace the "2" in "device = devices[2]" with your desired device from the step above.

#WebEx Token Refresh
If you're using a Personal Access Token, which expires in 12 hours, you can comment out or remove the def token_refresh() function.



