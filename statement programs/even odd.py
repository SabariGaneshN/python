sr=int(input("Enter starting range"))
er=int(input("Enter ending range"))
i=sr
e=0
o=0
for i in range(sr,er):
    if(i%2==0):
        e+1
    else:
        o+1
print("odd no.:",o)
print("even no,:",e)