#letra e de estrutura de dados
a=[]
b=[]
for i in range (5):
    a.append(int(input("Digite um valor para a lista A: ")))
    fatorial=1
    for j in range (1,a[i]+1):
        fatorial=fatorial*j
    b.append(fatorial)
print("Lista A: ",a)
print("Lista B: ",b)
