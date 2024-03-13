#programa que sorteia um número entre 1 e 38 sem se repetir e se repete ate queo usuario digite não
import random
lista = []
while True:
    numero = random.randint(1,38)
    if numero not in lista:
        lista.append(numero)
        print(numero)
        continuar = input("Deseja continuar? ")
        if continuar == "nao":
            break
    else:
        continue


