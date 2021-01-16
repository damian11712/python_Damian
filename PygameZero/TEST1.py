import pgzrun

WIDTH = 600
HEIGHT = 280

def draw():
    screen.fill("white")
    guitar.draw()

guitar = Actor("guitar.jpeg")
guitar.pos = (0, HEIGHT / 2)
speed = 0.5
v_g = 0.5


def update():
    """Changer des choses entre chaque mise à jour de la fenêtre"""
    guitar.x = guitar.x + speed
    guitar.x = guitar.x + v_g

pgzrun.go()