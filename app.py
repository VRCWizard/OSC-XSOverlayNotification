


from pythonosc import dispatcher
from pythonosc import osc_server
from XSONotifications import XSOMessage, XSNotifier




XSNotifier = XSNotifier()

# Define a function to handle incoming OSC messages
def message_handler(address, *args):
    #print(f"Received message from {address}: {args}")
    for arg in args:
        if isinstance(arg, str):
            if arg != "":
                print("OSC Message Received: ", arg)

                msg = XSOMessage()
                msg.messageType = 1
                msg.sourceApp = "TTS Voice Wizard"
                msg.opacity = 0.7 #silightly transulcent pick a value between 0.1 - 1.0
                msg.audioPath = "" #empty string prevents notification sound
                msg.content = arg #message variable
                msg.title = "TTS Voice Wizard" # The message title, you can replace the with your name for example
                msg.timeout = 5.0 #how long the message stays around, 5 seconds by default


                XSNotifier.send_notification(msg)
                break  # Exit the loop after processing the first string argument

# Create a dispatcher
dispatcher = dispatcher.Dispatcher()
# Map the message handler function to the OSC address "/test"
dispatcher.map("/chatbox/input", message_handler)


# Set up the OSC server
server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 9077), dispatcher)

print("OSC server started on port 9077...")
# Start the OSC server
server.serve_forever()