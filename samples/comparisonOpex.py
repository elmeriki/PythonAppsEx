Name_Enter = input("What is your name ?")

Names = len(Name_Enter)

if Names <= 3:

    print("Names is ok")

elif Names > 3 and not Names > 10:

    print("Name is also ok")
else:
    print("Name order is not ok ")

