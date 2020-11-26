import turtle
from rectangle import rectangle


def porte(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    '''
    turtle.fillcolor(couleur)
    turtle.penup()
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.pendown()
    turtle.end_fill()

if __name__ == '__main__':
    porte(70,70,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
                                