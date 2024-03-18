#calcula o somatorio dos grão de trigo de um tabuleiro de xadrez com while
cont=1
soma=0
while cont<=64:
    soma=(2**cont)-1
    cont+=1
print("O total de grãos de trigo é ",soma)
