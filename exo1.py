def vérifChiffres(l,n):
    '''(list, int) -> bool
    Verifie si la liste L de taille n contient que des nombres ou non 
    '''
    chiffre =True 
    for i in range(n) :  
        if l[i]/10< 1 :
            i+=1   
        elif (l[i]/10>=1):
            chiffre= False
    return chiffre

l=[]
n=len(l)
print(vérifChiffres([1,2,3,4,50,6,0],6))
