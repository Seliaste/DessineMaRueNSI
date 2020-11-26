from couleur_aleatoire import couleur_aleatoire
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    couleur1 = couleur_aleatoire()
    couleur2 = couleur_aleatoire()
    turtle.pencolor(couleur1)
    turtle.fillcolor(couleur2)
    turtle.penup() #on place le pinceau à la bonne position
    turtle.setposition(x-15,y) #c'est-à-dire 15 pixels avant l'abscisse vu que celle-ci correspond à la moitié de la fenêtre
    turtle.right(90) #on oriente le curseur 
    turtle.pendown() #là on peut commencer à tracer
    turtle.begin_fill()
    for i in range(4):  #on trace nos quatre bords consécutifs
        turtle.left(90)
        turtle.forward(30)
    turtle.end_fill()


if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()