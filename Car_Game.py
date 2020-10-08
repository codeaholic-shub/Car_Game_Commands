command=""
started=False
while True:
    command=input(">").lower()
    if command=="start":
     if started:
            print('Car is Already Started')
     else:
            started=True
            print("Your Car Has Started !")
    elif command=="stop":
     if not started:
        print("Your Car Has Already Stopped !")
     else:
        started=False
        print("Car Stopped ")
    elif command=="help":
        print('''
start- To start the car
stop- To stop the car
quit- To quit the programme
        ''')
    elif command=="quit":
     print("Quit ")
     break
    else:
        print("Something Unrealted Command ")

