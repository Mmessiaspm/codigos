#inserindo 10 numeros numa lista e imprimindo a lista
lista = []
for i in range(10):
    lista.append(int(input("Digite um número: ")))
    
print(lista)
#imprimindo a lista em ordem inversa
for i in range(9,-1,-1):
    print(lista[i])
    