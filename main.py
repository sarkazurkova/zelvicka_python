from turtle import *
import random

shape("turtle")
speed(10)

def flower():
    clear()
    pencolor("red")
    for i in range(200):
        forward(i)
        left(i+1)

def spirala(pocet, barva):
    clear()
    pencolor(barva)
    for i in range(pocet * 4):
        forward(i)
        left(90)

def kolecko(number):
    pencolor("green")
    circle(20)


def domecek():
    pencolor("green")
    i = 1
    for i in range(4):
        forward(100)
        right(90)
    left(60)
    forward(100)
    right(120)
    forward(100)



# vstup = vstup = input("1 - kyticka \n2 - spirala \n0 - konec porgramu\nvstup:")

# while(vstup !=0 ):
vstup = input("1 - kyticka \n2 - spirala\n3 - kolecko\n4 - domecek \n0 - konec porgramu\nvstup:")

if int(vstup) == 1:
    print("Vykresli se kyticka.\n")
    flower()
elif int(vstup) == 2:
    pocet = input("Pocet spiral:")
    barva = input("Zadej barvu, napr. blue, yellow, dark red, #33cc8c:")
    spirala(int(pocet), barva)
elif int(vstup) == 3:
    cislo = input("Zadejte cislo:")
    kolecko(int(cislo))
elif int(vstup) == 4:
    domecek()
elif int(vstup) == 0:
    print("Program bude ukoncen.")
    # break
else:
    print("Nebyl zadany platny znak.")


mainloop()
