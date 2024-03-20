# OSC-XSOverlayNotification
Send a string in an osc message to XSOverlay and receive a notification. Script created for deaf individual to be able to read messages sent by TTS Voice Wizard on another computer while in VR.

XSONotifications.py code from https://github.com/0xst4n/XSNotifications_discord


1. In TTS Voice Wizard set the OSC Send Port to 9077 the port the script is listening on

![image](https://github.com/VRCWizard/OSC-XSOverlayNotification/assets/101527472/50efaa8c-b8ec-4506-b449-ad0eb71d8d0d)

2. Set the ip for the XSNotifier to the IPv4 Address of a computer on the same network (wifi or ethernet)
   - To find the IPv4 Address open up **Terminal** on your computer and type ``ipconfig``
   - 127.0.0.1 will always send to localhost the computer running this script, so if you want to send to another computer use that computers IPv4 address

![image](https://github.com/VRCWizard/OSC-XSOverlayNotification/assets/101527472/eaaefe0e-6c90-468b-8e11-be6fbd5c926f)

3. Open terminal and type ``pip install python-osc``
4. Run the .bat file to run the script
