# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializa a lista de termos da PA e a soma
termos = []
soma = 0

# Calcula os 10 primeiros termos da PA
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    termos.append(termo_atual)
    soma += termo_atual

# Mostra os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:")
print(termos)

# Mostra a soma dos 10 primeiros termos
print("A soma dos 10 primeiros termos da PA é:", soma)