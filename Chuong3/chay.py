# n=int(input("Nhap so nguyen: (n>=1)"))
# i=2
# S=0
# while i<=n:
#     S=S+i
#     i=i+2
# print("Tong S=",S)
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print("*", end="")
        j=j+1
    print("")
    i=i+1