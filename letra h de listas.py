#ler uma valores inteiros em uma lista "a" e colocar em ordem decrescente numa lista "b"
a = []
b = []
for i in range(5):
    a.append(int(input("Digite um número para a lista A: ")))
for j in range(-1, -6, -1):
    b.append(a[j])
print("Lista A: ", a)
print("Lista B: ", b)