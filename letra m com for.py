#programa que le dez valores e apresenta a soma desses valores e a medias deles com for
soma = 0
for i in range(1,11):
    valor = int(input('Digite o valor: '))
    soma += valor
media = soma/10
print('A soma dos valores é: ',soma)
print('A media dos valores é: ',media)