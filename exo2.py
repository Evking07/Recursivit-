def initListe(L,n):
    for i in range(n):
        L.append(i)
       
    return L    

n=int(input("Entrez la valeur à ne pas atteindre : "))
L=[]
print(initListe(L,n))

    