#q1
def triangle(n): 
    '''int--->str'''
    '''fonction Python récursive appelée triangle qui prendra comme paramètre 
    un entier non négatif et qui générera un dessin composé d’étoile'''

   #Cas de base :
    if (n==1):
        print("*") 
    else:   #application de la récursivité:
        (n) * str(triangle(n-1))
        print(n* "*")
triangle(5)
