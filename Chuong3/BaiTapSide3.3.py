a=int(input("Tieu thu="))
if(a<=100):
    tien=550*a
if(101<=a<=150):
    tien=(100*550+ (a-100)*750)
if(151<=a<=200):
    tien=(100*550 + 50*750 + (a-100-50)*950)
if(a>=201):
    tien=(100*550 + 50*750 +50*950 + (a-100-50-50)*1350)
print("Thanh tien=", round(tien*(1+0.1),1),sep="")