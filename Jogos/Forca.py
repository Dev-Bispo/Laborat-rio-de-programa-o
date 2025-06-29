import math
import random

listapalavras = ["banana", "cama", "bola"]
palavra = random.choice(listapalavras)

letrasdescobertas = []

def printarpalavra(palavra, letrasdescobertas):
    x = 0
    atual = ""
    for i in palavra:
        if x in letrasdescobertas:
            atual = atual + "" +i
        else:
            atual = atual + " _"
        x += 1
    print(atual)

printarpalavra(palavra, letrasdescobertas)


erros = 0

while erros < 6 and len(letrasdescobertas) < len(palavra):
    letra = input("letra:")
    y = 0
    acertos=0
    for a in palavra:
        if a == letra:
            letrasdescobertas.append(y)
            acertos += 1
   
        y += 1
    if acertos == 0:
        erros += 1
        print('errou', erros, "/6 erros")
    printarpalavra(palavra, letrasdescobertas)

if erros >= 6:
    print("você perdeu, seu lixo")
elif len(letrasdescobertas) >= len(palavra):
    print("parabens")

   









