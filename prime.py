n=int(input("enter the number"))
if n<=1:
    print("invalid input ")
else:
    div=2
    while div<n:
        if n%div==0:
            print("not prime ")
            exit()
        else:
            div=div+1
    print("prime")    
     
