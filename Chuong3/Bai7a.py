while True:
    n=int(input())
    if(n<0):
        break
    if(n==0):
        print(1)
    else:
        res=i=1
        while(i!=n):
            i+=1
            res*=i
        print(res)
    

    
