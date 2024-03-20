#programa que impmpome o total do somatorio, medias e total dos numeros 
# lidos ate que seja um numwero negativo
soma = 0
cont=1
while True:
    num=int(input("Digite um numero: "))
    if num<0:
        break
    soma+=num
    media=soma/cont
    cont+=1
print("O somatorio dos valores e: ",soma)
print("A media dos valores e: ",media)
print("O total de valores lidos e: ",cont-1)