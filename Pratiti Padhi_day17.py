t=int(input())
for a in range(t):
    def lucky_no(n):
        d=sum=0
        while(n>0):
            d=n%10
            sum=sum+(d*d)    
            n=n//10            
        return sum            
    num=int(input())    
    res=num         
    while(res!=1 and res!=4):
        res=lucky_no(res)        
    if(res==1):
        print("lucky")   
    else:    
        print("unlucky")