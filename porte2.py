import  turtle

def porte2(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte dont le haut est un demi cercle
        La porte a une largeur totale de 30 pixels
        La partie rectangulaire a une hauteur de 40 pixels
        La partie semi circulaire a un rayon de 15 pixels
    '''
    turtle.fillcolor(couleur)
    turtle.penup()
    turtle.goto(x-15,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(40)
    turtle.circle(15,180)
    turtle.forward(40)
    turtle.end_fill()
    turtle.left(90)

if __name__ == '__main__':
    porte2(70,70,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()