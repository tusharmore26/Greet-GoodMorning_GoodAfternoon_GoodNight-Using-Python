import time

times=time.strftime('%H:%M:%S')
print("Current time is:",times)

hour=int(time.strftime('%H'))
mint=int(time.strftime('%M'))
sec=int(time.strftime('%S'))
print("Hour:",hour,"\nMinutes:",mint,"\nSeconds:",sec)

name=input("What is Your name:")

if((hour >= 4) and (hour<12)):
    print("\t\tGood Morning",name)
elif((hour >=12) and (hour<=14)):
    print("\t\tGood Afternoon",name)
elif((hour>14) and (hour<17)):
    print("\t\tGood Evening",name)
else:
    print("\t\tOk,Good Night,",name)



