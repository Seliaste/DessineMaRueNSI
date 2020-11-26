import turtle

def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle. Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    '''
    turtle.goto(x-(w/2),y)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    

if __name__ == '__main__':
    rectangle(50,50,150,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()