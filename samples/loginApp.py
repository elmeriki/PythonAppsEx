status = input("LOGIN APP. Press 1 to proceed 0 otherwise  ")
status = int(status)


if status ==  1:
    username =input("Create a username ")
    password = input("create a password ")
    print("You can proceed to login ")


    enterusername = input("Enter username ")
    enterpassword = input("Enter password ")

    if username == enterusername and password == enterpassword:
        print("Login is ok")


    else:
        enterusername = False
        enterpassword = False
        
        if enterusername == False  and enterpassword == False:

            exit= input("You  cant login press 1 to exit ")
            exit = int(exit)
            if exit == 1:
                print("Thank you bye")     
            
else:
    if status == 0:
        print("You cant proceed bye")
    
