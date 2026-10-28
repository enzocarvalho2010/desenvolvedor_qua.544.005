import os
import math

def li():
    os.system('cls' if os.name == 'nt' else 'clear')

def a_quad(b, h):
    return b*h

def a_circ(r):
    return math.pi*(r**2)

def cum_circ(r):
    return 2*math.pi*r