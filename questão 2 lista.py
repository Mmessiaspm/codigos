#programa que imprime a soma dos numros imares de uma lista de 5 numeros
a=[]
soma=0
for i in range(0,5):
    a.append(int(input("Digite um numero: ")))
    if a[i]%2!=0:
        soma+=a[i]
print("A soma dos numeros impares é: ",soma)
        
        