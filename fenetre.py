from rectangle import rectangle
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    turtle.setposition(x,y)
    turtle.forward(15)
    turtle.left(90)
    for i in range(3):
        turtle.forward(30)
        turtle.left(90)
    turtle.forward(15)


if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()