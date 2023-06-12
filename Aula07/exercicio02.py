base = float(input("Digíte a base do tríangulo: "))
while base <= 0:
    base = float(input("Digíte a base do triangulo > 0"))

while True:
    altura = float(input("Digite a altura do triangulo: "))
    if altura > 0:
        break

area = (base * altura) / 2
print(f"A área do triângulo é igual a {area:.2f}")