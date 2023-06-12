n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))
soma = n1 + n2
if soma > 1000:
    print(f"A soma dos seus números é {soma} que é maior que 1000!")
elif soma < 1000:
    print(f"A soma dos seus números é {soma} que é menor que 1000!")
else:
    print(f"A soma dos seus números foi igual a 1000!")