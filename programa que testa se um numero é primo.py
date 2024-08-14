#programa que testa se um dentro de uma faixa de numeros é primo
numero = int(input("Digite um número: "))
# programa que testa se um número dentro de uma faixa de números é primo
numero = int(input("Digite um número: "))

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Números primos na faixa:")
for i in range(2, numero + 1):
    if eh_primo(i):
        print(i)
