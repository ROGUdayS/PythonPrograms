import random
#Stop and wait 

def timer():
    clock=random.randint(1,15)
    return clock

def sender():
    no_of_frames=int(input("Enter number of frames to be sent :"))
    print("The Timeout is 10ms")
    for i in range(no_of_frames+1):
        clock_timed=timer()
        if(clock_timed<=10):
            print(i,": Frame is sent in ",clock_timed,"secs")
        else:
            print(i,": Frame is not sent")
            ack=0
            while(ack==0):
                clock_timed=timer()
                if(clock_timed<=10):
                    print(i,": Frame is sent in ",clock_timed,"secs")
                    ack=1
                else:
                    ack=0



        

sender()



#Go Back N
#Selective repeat