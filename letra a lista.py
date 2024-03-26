#ler dez numeros de uma lista e imprimi-los
a=[]
for i in range(1,11):
    a.append(int(input("Digite um numero: ")))

print(a)  
#reverte a ordem dos elementos da lista  
a.reverse()
print(a)