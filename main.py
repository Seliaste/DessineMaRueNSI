import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(800, 600)
    turtle.speed(50)
    # On définit la hauteur du sol
    y_sol = -200
    # Dessin du sol de la rue
    sol(y_sol)
    # Dessin des 4 immeubles
    for i in range(4):
        turtle.pensize(1)
        immeuble(-220+i*160,y_sol)
        


    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main()



