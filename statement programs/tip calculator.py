fr=int(input("enter a number must be 1-5"))
se=int(input("enter a number must be 1-5"))
am=int(input("enter a number must be 1-5"))
amount=int(input("enter a number "))
if(fr in[4,5]):
   if(se in [4,5] and am in [4,5]):
       print(f"tip is ",am*(10/100))
   elif(se in [3,2,1] and am in [3,2,1]):
       print(f"tip is ",am*(5/100))
if(fr in[3,2,1]):
   if(se in [4,5] and am in [4,5]):
       print(f"tip is ",am*(5/100))
   elif(se in [3,2,1] and am in [3,2,1]):
       print(f"tip is",am*(1/100))
