#programa que immprime cinco vezes um numero lido multiplicado por 3
resp="sim"
while resp=='sim':
    num=int(input("Digite um numero: "))
    r=num*3
    print(r)
    resp=input("Deseja continuar? ")
    if resp!="sim":
        break
print("Fim do programa")