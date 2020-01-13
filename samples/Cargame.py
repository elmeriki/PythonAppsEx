message = input("Type help to continue ? ")

startmessage  = "start" 
stopmessage = "stop"
quitmessage = "quit" 

if message == "help" or message == "HELP" or message == "Help":
    print("""     
    start - to start the car
    stop - to stop the car
    quit - to exit
    """)
data = input(str(">"))
if data == startmessage:
        print("The car is now moving ")
elif data == stopmessage:
    print("Tha car stop Moving")
else:
    data == quitmessage
    print("Thank you and Bye")

    