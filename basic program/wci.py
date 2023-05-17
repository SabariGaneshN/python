import math
v=float(input("Enter windspeed in KMPH"))
t=float(input("Enter temperature in CELSIUS"))
wci=13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
wci=round(wci)
print("Wind chill index is: ",wci)
