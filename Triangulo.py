#programa que testa se tres numeros formam um triângulo
#lendo os lados do traingulo
a=int(input("Digite o lado a: "))
b=int(input("Digite o lado b: "))
c=int(input("Digite o lado c: "))
#testando se os lados formam um triângulo
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("Triângulo equilátero")
    elif a==b or a==c or b==c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os lados não formam um triângulo")
