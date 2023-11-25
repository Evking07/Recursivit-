# Recursivit-

19
 
Récursivité
1
Exercice 1
• Écrivez une fonction Python récursive nommée vérifChiffres, pour vérifier 
si tous les éléments aux positions 0...N-1 d’une liste d’entiers (A) sont des 
chiffre (entre 0 et 9).
• La fonction prend deux paramètres, une référence à la liste et un entier qui 
est initialement la taille de la liste.
• Faire l’appel de cette fonction dans le programme principal
17

Exercice 2
• Écrivez une fonction Python récursive nommée initListe pour créer une liste 
contenant les valeurs de 0 à n-1. 
• La fonction prend deux paramètres, une référence à la liste et un entier qui est la 
valeur n.
Dans le program principal il faut :
- initialiser une liste (L = [])
- faire l’appel à la fonction récursive initListe avce cette liste L, pour la modifier
- et, demander à l’usager d’entrer la valeur n à partir du clavier
18
Exercice 3 – Algorithme d’Euclide
• Le Plus Grand Commun Diviseur (PGCD) de deux nombres entiers est le plus grand entier qui divise les deux nombres avec un reste nul.
• L’algorithme d’Euclide pour trouver le PGCD de x et y est:
pgcd(x,y) est ...  
   y   si x ≥ y et x mod y est 0
   pgcd(y, x)    si x < y
   pgcd(y, x mod y)      autrement
• Si x ≥ y, alors l’algorithme devient
 pgcd(x, y) est   ... 
  y   si x mod y est 0
  pgcd(y, x mod y)  autrement
    Ça marche même si x < y. Le premier appel récursive échange l’ordre à y, x 
19
Exercice 3 - Algorithme d’Euclide
• Écrivez une fonction Python récursive nommée pgcd, pour trouver et 
retourner le Plus Grand Commun Diviseur (PGCD) de deux nombres x et y 
passés en paramètres.
• Testez-lapgcd(1234,4321)
pgcd(8192,192)
...
20
