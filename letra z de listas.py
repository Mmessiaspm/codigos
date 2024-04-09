#programa que conta a quantidade de elementos impares de um lista e calcula o percentual de elementos impares
a=[]
impar=0
total=0
for i in range(10):
    a.append(int(input("Digite um número: ")))
    if a[i]%2!=0:
        impar+=1
    total+=1
print("A quantidade de elementos impares é: ",impar)
print("O percentual de elementos impares é: ",(impar/total)*100,"%")
