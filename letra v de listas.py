#contar elementos pares e imares de uma dada lista
a=[]
par=0
impar=0
for i in range(10):
    a.append(int(input("Digite um número: ")))
    if a[i]%2==0:
        par+=1
    else:
        impar+=1    
print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")
