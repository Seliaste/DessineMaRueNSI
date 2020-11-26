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
    turtle.colormode(255)
    # Dessine la facade
    facade(x,y_sol,c_facade,0)
    # Construit les 3 éléments (1 porte et 2 fenetres)

    i = randint(1,3)
    if i == 1:
        fenetre(x-40,10)
        penup()

        pendown()
        fenetre(x,10)
        penup()

        pendown()
        porte(x+40,0,"red")
        penup()

    elif i == 2:
        fenetre(x-40,10)
        penup()

        pendown()
        porte(x,0,"red")
        penup()

        pendown()
        fenetre(x+40,10)
        penup()
        print(2)

    elif i == 3:
        porte(x-40,0,"red")
        penup()

        pendown()
        fenetre(x,10)
        penup()

        pendown()
        fenetre(x+40,10)
        penup()      
        print(3)



if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()