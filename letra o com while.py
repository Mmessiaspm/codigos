#programa que imprime o fatorial dos numeros impares de 1 a 10 com while
cont=1
while cont<=10:
    if cont%2!=0:
        fatorial=1
        cont2=1
        while cont2<=cont:
            fatorial*=cont2
            cont2+=1
        print(fatorial)
    cont=cont+1