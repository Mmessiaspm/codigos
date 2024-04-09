#programa que apresenta a menor a maior e a media das temperaturas em graus celsius
a=[]
for i in range(10):
    a.append(float(input(f"Digite a {i+1}o. temperatura em graus celsius: ")))
a.sort()
print("A menor temperatura é: ",a[0])
print("A maior temperatura é: ",a[9])
print("A média das temperaturas é: ",sum(a)/10)

    