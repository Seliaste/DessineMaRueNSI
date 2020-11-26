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
    turtle.setposition(x,y) 
    turtle.left(90)  #nos coordonnées correspondent à une abscisse du centre de la fenêtre, et à une ordonnée étant le sol du niveau
    turtle.forward(20) #on doit donc rejoindre le bord d'une fenêtre en tournant de 90° puis en avançant de la distance entre le sol et le bas de la fenêtre (j'ai mis 20 px je n'étais pas sûre vu qu'il n'y avait pas vraiment de valeur)
    turtle.pendown() #là on peut commencer à tracer
    turtle.begin_fill()
    turtle.right(90) #on oriente le curseur 
    turtle.forward(15) #on avance que de la moitié vu que notre abscisse est à la moitié de la fenêtre
    for i in range(3):  #on trace nos trois bords consécutifs
        turtle.left(90)
        turtle.forward(30)
    turtle.left(90) #et on finit par tracer la première moitié que nous n'avions pas pu faire au début
    turtle.forward(15)
    turtle.end_fill()


if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()