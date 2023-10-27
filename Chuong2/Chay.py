def nhap_canh():
    while True:
        a = float(input("cạnh thứ 1 là: "))
        b = float(input("cạnh thứ 2 là: "))
        c = float(input("cạnh thứ 3 là: "))         
        if ((a > 0 and b > 0 and c > 0) and (a + b > c and b + c > a and a + c > b)):
            return a, b, c
        else:
            print("Khong hop le")
def tam_giac(a, b, c):
    hop = [a, b, c] 
    canh_huyen = max(hop)
    canh1 = min(hop)
    canh2 = sum(hop) - canh_huyen - canh1
    if canh1**2 + canh2**2 == canh_huyen**2:
        if canh1 == canh2:
            print("đó là 1 tam giác vuông cân!!!")
        else:
            print("đó chỉ là tam giác vuông!")
    else:
        print("đây không phải tam giác vuông")
a, b, c = nhap_canh()
tam_giac(a, b, c)