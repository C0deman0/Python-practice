#this code print how many weeks months days left if we live until 90
age=input("enter your age : ")
ageLeft=90-int(age)
days=ageLeft*365
weeks=ageLeft*52
months=ageLeft*12
print(f"you have {days}days, {weeks}weeks, {months}months left")