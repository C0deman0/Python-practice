#bmi calculator
weight=int(input("enter your weight in kg : "))
height=float(input("enter your height in m : "))
bmi=weight/(height**2)
print(f"your bmi is : {round(bmi)}")