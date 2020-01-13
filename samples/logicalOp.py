credit_status =input("How is your Credit status reply 1 if ok and 0 other wise ? ")
high_income =input("what is your average salary  ? ")

credit_status = int(credit_status)
high_income = int(high_income)

if credit_status == 1 and high_income > 9000:
    print("You are eligable for a loan")

elif credit_status == 0  and high_income < 9000:
    print("You are not aligible for a loan")

else:
    print("You dont qualify at ALL sorry ")

    