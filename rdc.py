from facade import facade
from random import shuffle
from porte import porte
from fenetre import fenetre
import turtle
from turtle import*
from random import*

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
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
        print(3)

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()