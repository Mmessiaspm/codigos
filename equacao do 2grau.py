#programa que calcula as raizes de uma equação do segundo grau
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
#calculo do delta
delta=b**2-4*a*c
#calculo das raizes
x1=(-b+(delta**0.5))/2*a
x2=(-b-(delta**0.5))/2*a

if a!=0 and b!=0 and c!=0:
    if delta>0:
        print("As raizes da equação são",x1,"e",x2)

    if delta==0:
        print("A raiz desta equação é",x1,x2)

    if delta<0:
        print("Esta equação não possui raízes reais")
else:
    print("Esta equação não é do segundo grau")

