
def hospital(weight,hight):

    if weight > 90 and hight > 90:
        print("you weight is tomuch sir")

    elif weight < 40 and hight < 40:
        print("You are very sick")

    else:
        print("you are almost dying")
    

weight = input("what is your hieght? ")
weight = int(weight)
hight=input("what is your height? ")
hight = int(hight)
hospital(weight,hight)


        

