#programa que busca um elemento em uma lista sem usar o comando in
lista = [1,2,3,4,5,6,7,8,9,10]
resp='sim'
while True:
    achou=False
    n=int(input('Digite um número para buscar na lista: '))
    cont=0
    while cont<len(lista):
        if lista[cont]==n:
            achou=True
            break
        cont+=1
    if achou:
        print('O número',n,'foi encontrado na posição',cont+1)
    else:
        print('O número',n,'não foi encontrado na lista')
    resp=input('Deseja buscar outro número? ')
    if resp=='não':
        break
print('Fim do programa')