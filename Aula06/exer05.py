tipo = input("Qual tipo de combustível você deseja utilizar? A(alcool) D(diesel) G(gasolina) ")
litros = float(input("Quantos litros vão ser colocados? "))
if tipo.upper() == "A":
    preco = litros * 1.7997
    print(f"O preço que vai ser pagado utilizando Alcool vai ser R${preco:.2f}")
elif tipo.upper() == "D":
    preco = litros * 0.9798
    print(f"O preço que vai ser pagado utilizando Diesel vai ser R${preco:.2f}")
elif tipo.upper() == "G":
    preco = litros * 2.1009
    print(f"O preço que vai ser pagado utilizando Gasolina vai ser R${preco:.2f}")
else:
    print("Tipo de combustível inválido")