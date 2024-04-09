#ler cinco elementos em uma lista "a" implicando em o 
# somatorio de cada elemento de "a" em uma lista "b"
a = []
b = []
for i in range(5):
    a.append(int(input("Digite um número: ")))
    somatorio=0
    for j in range(a[i]+1):
        somatorio+=j
    b.append(somatorio)
print(a) 
print(b)