#programa que recebe numeros pares para lista a e numeros impares para lista b, e junta as duas em uma lista c
a,b,c=[],[],[]
#atribuindo elementos a lista a
cont=0
print("Inserindo elementos da lista a")
while cont<6:
    n=(int(input("Digite um numero par: ")))
    if n%2==0:
        a.append(n)
        cont+=1
    else:
        print("Numero impar")
#atribuindo elementos a lista b
print("Inserindo elementos da lista a")
cont=0
while cont<6:
    n=(int(input("Digite um numero impar: ")))
    if n%2!=0:
        b.append(n)
        cont+=1
    else:
        print("Numero par")
c=a+b
print(c)