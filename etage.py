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
    
    # Dessine la facade
    facade(x,y_sol,couleur,niveau)
    i = randint(1,2)
    print(i)
    if i == 1:
        fenetre(x-60,y_sol+niveau*60+10)
    elif i == 2:
        fenetre_balcon(x-60,y_sol+niveau*60+10)
    i = randint(1,2)
    print(i)
    if i == 1:
        fenetre(x-20,y_sol+niveau*60+10)
    elif i == 2:
        fenetre_balcon(x-20,y_sol+niveau*60+10)
    i = randint(1,2)
    print(i)
    if i == 1:
        fenetre(x+30,y_sol+niveau*60+10)
    elif i == 2:
        fenetre_balcon(x+30,y_sol+niveau*60+10)
        

if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()