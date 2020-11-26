import turtle

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.up() #on leve le crayon
    turtle.setposition (x,y_sol) #on se met a la position donne dans toit
    turtle.fillcolor("black") #on remplie le dessin qui va etre fait
    turtle.begin_fill() #on commence le remplissage
    turtle.down() #on ecrit
    turtle.forward(160) #on avance en avant de 160
    turtle.left(155) #on tourne de 155 degrees vert la la gauche
    turtle.forward(89) #on avance de 89
    turtle.left(50) #on tourne de 50 degrees a gauche
    turtle.forward(89) #on avance de 89 
    turtle.left(155) #on tourne de 155 degrees
    turtle.end_fill() #on fini le remplissage
    turtle.up() #on leve le crayon

if __name__ == '__main__':
    toit1(70,70,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()