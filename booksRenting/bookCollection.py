import datetime 
from datetime import date


def collectingNamesandBookinDuration():
    names=input("what is your names?  ")
    proceed_value = input("Do you acept the Terms and Conditions y(Yes) and N (No) ")
    if names != "" and proceed_value == "Y" or proceed_value =="y":
        print("This is ok")
    else:
        print("You must acept the terms and conditions to proceed")



def displayTodaysDate():
    todays_date = datetime.date.today()
    display = "Hello {} the date of today is {}"
    print(display.format(names,todays_date))


def CollectiomDuration():
    duration=input("How long do you want to borrow the book? ")
    duration=int(duration)
    returndate = datetime.timedelta(days=duration)
    daterr = todays_date - returndate
    dis = " The book must be return on of before  {} "
    print(dis.format(daterr))

def Display():

    if collectingNamesandBookinDuration() == True and displayTodaysDate() == True:
        CollectiomDuration()

    

        
        
Display()
    
