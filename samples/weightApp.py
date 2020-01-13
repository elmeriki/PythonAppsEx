weightt = input("Enter weight ?")
weight_typee =  input ("Press L for Pounds Wrught and K for kilograms ? ")

weight = int(weightt)

weight_type = str(weight_typee)

Poundweight = weight * 0.45

kiloweight = 0.45  / weight

if weight_type == "L" or weight_type == "l":
    print(f"Your weight in Pound is :{Poundweight}P")

elif weight_type == "K" or weight_type == "k":
    print(f"Your weight in Kg is :{kiloweight}Kg")
else:
    print("We cant get your weight")

    




 

