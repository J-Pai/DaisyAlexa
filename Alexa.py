# Import standard python modules.
import sys
import time
import serial

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY      = '317bca24bd7a4e89ba35110c24190573'
ADAFRUIT_IO_USERNAME = 'tewodros'  

"""
So some tips and tracking strategies that you all can utilize is 
First typically a higher frame-rate equates to better performance and accuracy 
You should try decreasing resolution and the size of the bbox to avoid having parts of the background in the set
Avoid using cv2.resize() if possible 
Also with drifting and recovery there are alot of pros and cons that come with every tracker. with no one perfect tracker.
Some solutions include 
-having bbox checks
-using multiple trackers and having them check one another 
You should also consider using the KCF trackers it is one of the best options out there
Lastly eliminate unnecessary information from the initial bounding box to achieve better performance and tracking 
"""
"""
def passByte(b):
    print("Passing byte " + str(b))
    ser.write(bytes([int(b)]))

def halt():
    passByte(0)

def moveForward():
    passByte(1)

def turnRight():
    passByte(2)

def turnLeft():
    passByte(3)

def moveBackward():
    passByte(4)
"""
def connected(client):
    print('Connected to Adafruit IO!  Listening for Daisy changes...')
    # Subscribe to changes on a feeds like daisy stop and move forward.
    client.subscribe('daisy-call')
    

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):

    
    """
    case = int(payload)                               # associate payload value with daisy commands                   
    if case == 0:
       # halt()          
        print('Daisy has now stopped moving')

    elif case == 1:
       # moveForward()
        print('Daisy has now started moving forward')
"""



# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received. 
# Run a thread in the background so you can continue running script
client.loop_background()

msg = "Hello this is Daisy"
client.publish('daisy-call', msg)

while True:
    time.sleep(10)

if __name__ == "__main__":
    main()
