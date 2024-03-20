#programa que imprime o fatorial dos numeros impares de 1 a 10 com for
for i in range (1,11,2):
    fatorial=1
    for j in range (1,i+1):
            fatorial*=j
    print(fatorial)
    