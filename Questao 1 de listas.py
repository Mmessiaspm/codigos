'''Ler elementos para um alista A e criar uma lista B, seguido a seguinte lei dei de criaçao
se o indice de A for par multiplica a 5 e se for impar soma por 5'''
a=[]
b=[]
for i in range(0,5):
    a.append(int(input(f"Digite o {i+1}º numero: ")))
    if i%2==0:
        b.append(a[i]*5)
    else:
        b.append(a[i]+5)
print(a)
print(b)