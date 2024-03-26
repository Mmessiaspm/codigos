#letra b de estrutura de dados
a=[]
b=[]
for i in range(0,8):
    a.append(int(input(f"Digite o {i+1} elemento de número A: ")))
    b.append(a[i]*3)
print(f"O vetor B é: {b}")    
    
