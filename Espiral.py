from turtle import *

#Aqui ajustamos el cuadrado
def cuadrado(longitud):
    for i in range(4):
        forward(longitud)
        right(90)

#Aqui ajustamos la espiral
def espiral():
    for i in range(72):
        cuadrado(100)
        right(5)

def exit():


speed(0)

espiral()

done()
