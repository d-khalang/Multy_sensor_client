from MyMQTT import *
from simpleSubscriber import MySubscriber
import time


if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    name = input("Your name: ")
    myClient = None
    while True:
        search = input("""How would you like to see the sensors data?
                '1' for Data from all the sensors of the building
                '2' Data from all the sensors on a single floor
                '3' Data from a sensor in a particular room
                'q' to quite\n\n""")
        
        if search == 'q':
            if myClient:
                myClient.stop()
            break 

        if search == '1':
            topic = name +"/"+conf["baseTopic"]+"/#"
        elif search == '2':
            floorID = input("Floor: ")
            topic = name +"/"+conf["baseTopic"]+"/"+ floorID + "/#"
        elif search == '3':
            roomID = input("Room: ")
            topic = name +"/"+conf["baseTopic"]+ "/+/" + roomID + "/#"

        if myClient:
            myClient.stop()

        myClient = MySubscriber("danikh", topic, conf['broker'])
        myClient.start()
        
        a = 0
        while a < 10:
            time.sleep(1)
            a += 1

        