def pgcd(x,y):
    if (x >= y) and ( x%y==0):
        if x%y==0:
            return y 
        else:
            pgcd(y, x%y)
    elif x<y:
        x=y        
        return pgcd(x,y)
       
    else: 
        x=y
        return pgcd(x,x%y)
        

print(pgcd(1234,4321))
    
