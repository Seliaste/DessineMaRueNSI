import turtle
from rectangle import rectangle


def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
    h=60
    turtle.color(couleur)
    if niveau == 0:
        turtle.up()
        turtle.goto(x,y_sol)
        turtle.pendown()
        turtle.begin_fill()
        rectangle(x,y_sol,140,h)
    if niveau == 1:
        turtle.up()
        turtle.goto(x,y_sol+h)
        turtle.pendown()
        turtle.begin_fill()
        rectangle(x,y_sol+h,140,h)
    if niveau == 2:
        turtle.up()
        turtle.goto(x,y_sol+h*2)
        turtle.pendown()
        turtle.begin_fill()
        rectangle(x,y_sol+h*2,140,h)
    if niveau == 3:
        turtle.up()
        turtle.goto(x,y_sol+h*3)
        turtle.pendown()
        turtle.begin_fill()
        rectangle(x,y_sol+h*3,140,h)
    if niveau == 4:
        turtle.up()
        turtle.goto(x,y_sol+h*4)
        turtle.pendown()
        turtle.begin_fill()
        rectangle(x,y_sol+h*4,140,h)
    turtle.end_fill()


if __name__ == '__main__':
    facade(70,70,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()