# number = [11,43,30,52,52,2,123]
# for num in number:
#     if num % 5 ==0:
#         print(num)
#         break
# else:
#     print("Nothing was found")
        
# Finding Prime Number:
    
num =11
for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")