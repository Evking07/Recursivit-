
#q2
def etoiles(n): 
    '''int--->str'''
    '''fonction Python récursive appelée etoiles qui prendra comme paramètre un entier non 
    négatif et qui générera un dessin composé d’étoiles. 
    Il affiche une série de triangle à l'endroit et à l'envers'''

    #cas de base:
    if (n==1):
        print("*") 
        print("*")
    else:   #application de la récursibvité
            print(n * "*")    
            s= n * str(etoiles(n-1))
            print(n * "*")           
etoiles(4)
    
