import datetime 
from datetime import date


names=input("what is your names?  ")
proceed_value = input("Select 1 to rent or 0 to exit ")

def bookCollection():
    
    if(names == names):
        todays_date = datetime.date.today()
        display = "Hello {} the date of today is {}"
        print(display.format(names,todays_date))
        duration=input("How long do you want to borrow the book? ")
        duration=int(duration)
        returndate = datetime.timedelta(days=duration)
        daterr = todays_date - returndate
        dis = " The book must be return on of before  {} "
        print(dis.format(daterr))

bookCollection()


