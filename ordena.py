a= int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))
c=int(input("digite o terceiro número: "))

if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>b:
    a,b = b,a
print(a,b,c)

