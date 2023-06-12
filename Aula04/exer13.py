salario = float(input("Entre com o valor do salário mínimo: "))
quilowatts_hora = float(input("Entre com o valor de quilowatts: "))
quilowatts = salario / 8
valor = quilowatts * quilowatts_hora
desconto = valor = (valor * 0.15)

print(f"O valor de cada quilowatt é {quilowatts}, o valor a ser pago pela residencia é R${valor} e esse valor desconto de 15% é R${desconto}")
