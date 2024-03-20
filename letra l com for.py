#programa que calcula  a soma do fatorial de 15 numeros com for
soma=0
for i in range(1,16):
    fatorial=1
    for j in range(1,i+1):
        fatorial*=j
    soma+=fatorial
print("O somatorio dos fatorial de 1 a 15 e: ",soma)