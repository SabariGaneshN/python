n=input("enter a name")
a=int(input("enter a age "))
g=input("enter a M or F")
if(a>=18 and a<30 and g=='M'):
    print("wages charge is 700")
if(a>=18 and a<30 and g=='F'):
    print("wages charge is 750")
elif(a>=30 and a<=40 and g=='M'):
    print("wages charge is 800")
elif(a>=30 and a<=40 and g=='F'):
    print("wages charge is 850")
