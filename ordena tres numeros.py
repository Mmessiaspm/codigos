#programa que ordena tres numeros em ordem crescente
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
if a>b and a>c:
    if b>c:
        print("A ordem crescente é",c,b,a)
    else:
        print("A ordem crescente é",b,c,a)
if b>a and b>c:
    if a>c:
        print("A ordem crescente é",c,a,b)
    else:
        print("A ordem crescente é",a,c,b)
if c>a and c>b:
    if a>b:
        print("A ordem crescente é",b,a,c)
    else:
        print("A ordem crescente é",a,b,c)
