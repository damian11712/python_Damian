
"""Snake, classic arcade game.
Exercises

1. Comment rendre le serpent plus rapide ou plus lent?
2. Comment pouvez-vous faire passer le serpent sur les bords?
3. Comment déplaceriez-vous la nourriture?
4. Changez le serpent pour qu'il réponde aux touches fléchées.

"""
WIDTH = 600
HEIGHT = 580

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

