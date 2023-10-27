a=input("Ho ten: ")
b=int(input("So ngay cong: "))
c=int(input("Don gia ngay cong: "))
d=float(input("He so phu cap: "))
e=int(input("Tam ung: "))
Luong = c *b * d
Thuc_linh = Luong - e
print("Nhan vien ",a,",", " Co tien Luong=",round(Luong,1),","," Tam ung=",e, " va Thuc linh=", round(Thuc_linh,1), sep="")