import turtle
from rectangle import rectangle
from trait import trait
from couleur_aleatoire import couleur_aleatoire

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    #fenetre
    turtle.colormode(255)
    turtle.fillcolor(couleur_aleatoire())
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.end_fill()
    # balcon
    turtle.pencolor('black')
    for i in range(10):
        rectangle(x+(3*i)-15,y,3,20)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()