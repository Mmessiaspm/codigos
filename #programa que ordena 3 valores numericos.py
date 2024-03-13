#programa que ordena 3 valores numericos em ordem crescente
#autor: Marcos César Martins
#data: 10/10/2019
a=int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
c=int(input("Digite o terceiro valor: "))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
    