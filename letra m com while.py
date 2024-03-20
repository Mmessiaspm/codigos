#programa que le dez valores e apresenta a soma desses valores e a medias deles com whule
soma = 0
cont=1
while cont<=10:
    valor = int(input('Digite o valor: '))
    soma += valor
    cont += 1
media = soma/10
print('A soma dos valores é: ',soma)
print('A media dos valores é: ',media)