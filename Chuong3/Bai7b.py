while True:
    n=int(input())
    if(n<0):
        break
    if(n==0):
        print(1)
    else:
        res=i=1
        for i in range (1,n,1):
            i+=1
            res*=i
        print(res)

    