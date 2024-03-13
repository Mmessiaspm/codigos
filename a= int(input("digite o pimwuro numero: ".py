a= int(input("digite o pimwuro numero: "))
b= int(input("digite o segundo numero: "))
c= int(input("digite o terceiro numero: "))

if a > b:
    a,b=b,a
if b>c:
    b,c=c,b
print(a,b,c)