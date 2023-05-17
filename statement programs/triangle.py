import math
a=int(input("Enter length of side a"))
b=int(input("Enter length of side b"))
c=int(input("Enter length of side c"))
if(a==b+c and b==c+a and c==a+b):
    print("Triangle is possible")
else:
    print("Triangle not possible")
    
