t=1
while(t<2):
    n=int(input("enter number:"))
    if n>1:
        for i in range(2,int(n/2)+1):
            if (n % i) == 0:
                print(n,"is not a prime")
                break
        else:
            print(n,"is a prime")
    else:
        print(n,"is not a prime")
    if(n==-1):  #to break the infinite loop
        break    
    
                
           