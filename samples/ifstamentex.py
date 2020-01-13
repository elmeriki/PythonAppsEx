price = 1000
Credit_status = input("What is your credit score reply 1 if good and 0 otherwise ?")
Credit_status = int(Credit_status)

if Credit_status == 1:
    donwpayment = price * 0.1

    print(f"You need a down payment of : ${donwpayment}")

elif Credit_status == 0:
    donwpayment = price * 0.2
    
    print(f"You need a down payment of : ${donwpayment}")

else:
    print(" You dont qualify for a credit ")


