#busca binaria
a = [91,81,77,62,22,21,14,10,8,7,4]
#ordenando a lista com o bublesort
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
inicio=0
fim=len(a)-1
meio=(inicio+fim)//2
x=22
while inicio<=fim and a[meio]!=x:
    if x<a[meio]:
        fim=meio-1
    else:
        inicio=meio+1
    meio=(inicio+fim)//2
if a[meio]==x:
    print("elemento encontrado na posição",meio)    
else:    
    print("elemento não encontrado")
print("fim do programa")