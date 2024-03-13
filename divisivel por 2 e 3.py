#Ler quatro valores numéricos inteiros e apresentar os valores que são divisíveis por 2 e 3.
#Se não existir nenhum valor que atenda a condição, apresentar uma mensagem informativa.
#Entrada: Quatro valores inteiros
#Saída: Valores divisíveis por 2 e 3 ou mensagem informativa
#Observação: A saída deve seguir a ordem de leitura dos valores
a=int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
c=int(input("Digite o terceiro valor: "))
d=int(input("Digite o quarto valor: "))
if a%2==0 and a%3==0:
    print(a)
if b%2==0 and b%3==0:
    print(b)
if c%2==0 and c%3==0:
    print(c)
if d%2==0 and d%3==0:
    print(d)
if a%2!=0 and a%3!=0 and b%2!=0 and b%3!=0 and c%2!=0 and c%3!=0 and d%2!=0 and d%3!=0:
    print("Nenhum valor atende a condição.")
    