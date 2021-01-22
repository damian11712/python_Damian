import pgzrun

WIDTH = 600
HEIGHT = 580

guitar = Actor("guitar.jpeg")
guitar.pos = (WIDTH/2, HEIGHT/2)
speed = 1


def draw():
    screen.fill("white")
    guitar.draw()

def on_mouse_move(rel):
    guitar.x += rel[0]
    guitar.y += rel[1]

pgzrun.go()