from random import randint
from toit1 import toit1
from toit2 import toit2
import turtle

def toit(x, y_sol, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Cette fonction dessine au hasard un des 2 types de toit

    '''
    n = randint(1,2)
    if n == 1 :
        toit1(x-70,y_sol+niveau*60+60,niveau)
    if n == 2 :
        toit2(x-70,y_sol+niveau*60+60,niveau)

if __name__ == '__main__':
    toit(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()