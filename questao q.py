#programa que calcula a area total de uma casa
arealTotal=0
resp='sim'
while resp!='nao':
    comodo=input('Digite o comodo: ')
    largura=float(input('Digite a largura do comodo: '))
    comprimento=float(input('Digite o comprimento do comodo: '))
    areaComodo=largura*comprimento
    print('A area do comodo',comodo,'é',areaComodo)
    arealTotal+=areaComodo
    resp=input('Deseja continuar? ')
    if resp=='nao':
        break
print('A area total da casa é',arealTotal)