from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    facade(x,y_sol,c_facade,c_porte)
    # Construit les 3 éléments (1 porte et 2 fenetres)
    i = 3 #randint(1,3)
    print(i)
    if i == 1:
        penup()
        forward(10)
        left(90)
        forward(10)
        pendown()
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        penup()

        forward(10)
        pendown()
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        penup()
        
        forward(35)
        right(90)
        forward(10)
        left(90)
        pendown()
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        left(90)
        forward(50)
        penup()

        print(1)
    elif i == 2:
        penup()
        forward(10)
        left(90)
        forward(10)
        pendown()
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        penup()

        forward(10)
        right(90)
        forward(10)
        left(90)
        pendown()
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        penup()

        forward(35)
        left(90)
        forward(10)
        right(90)
        pendown()
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        penup()
        print(2)


    elif i == 3:
        penup()
        forward(10)
        pendown()
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        penup()

        forward(35)
        left(90)
        forward(10)
        pendown()
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        penup()

        forward(10)
        pendown()
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(30)
        penup()      
        print("i=3")
    # dessin des 3 Eléments
    pass

if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()