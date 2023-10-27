x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
if (ch== "+"or ch== "-"or ch== "*"or ch== "/"):
    if (ch=="+"):
        print(x,ch,y,"=",x+y,sep="")
    if (ch=="-"):
        print(x,ch,y,"=",x-y,sep="")
    if (ch=="*"):
        print(x,ch,y,"=",x*y,sep="")
    if (ch=="/"):
        if(y!=0):
            print(x,ch,y,"=",x/y,sep="")
        else:
            print ("Khong hop le")
else:
    print("Khong hop le")

