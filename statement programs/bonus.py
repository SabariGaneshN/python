salary=int(input("enter a salary "))
year=int(input("enter a salary "))
if(year>10):
    b=(salary*10/100)
    print("salarybonus",b)
elif(year>6 and year<10):
    b=(salary*8/100)
    print("salarybonus",b)
else:
    b=(salary*5/100)
    print("salarybonus",b)
