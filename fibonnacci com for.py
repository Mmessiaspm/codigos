#programa que imprime os dez primeiros numeros da serie de fibonnacci com  for
primeiro = 1
segundo = 1
print(primeiro)
print(segundo)
for cont in range(1,14):
    proximo = primeiro + segundo
    print(proximo)
    primeiro = segundo
    segundo = proximo
print("Fim da serie de Fibonacci")