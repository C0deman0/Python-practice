#this is bill spliter
print("welcome to the billsplitter")
totalBill=int(input("enter the total amount of bill : "))
peoples=int(input("enter the total number of peoples : "))
split=totalBill/peoples
print(f"amount for each person is $ : {round(split,2)}")
addTip=input("do you wanna add tip? y/n : ")
if addTip=="y":
    tip=int(input("enter the percentage of tip you wanna give : "))
    tip=totalBill*(tip/100)
    totalBill=totalBill+round(tip)
    split=totalBill/peoples
    print(f"tip is : $ {tip} ")
    print(f"amount for each person is : $ {round(split,2)}")
else:
    print("thanks for using billspliter")


    


