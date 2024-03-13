salario=float(input("Digite o salário: "))
if salario<500:
    salario=salario*1.15
else:
    if salario<=1000:
        salario=salario*1.10
    else:
        salario=salario*1.05
print("O salário é: ",salario)
