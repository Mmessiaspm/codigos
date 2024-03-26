#letra c estrutura de dados
a=[]
b=[]
c=[]
for i in range(5):
    a.append(int(input(f"Digite o {i+1} número de A: ")))
    b.append(int(input(f"Digite o {i+1} número de B: ")))
    c.append(a[i]-b[i])
print(c)
    
