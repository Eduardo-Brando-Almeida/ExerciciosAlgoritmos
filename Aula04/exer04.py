nasc = int(input("Digite o seu ano de nascimento: "))
atual = int(input("Digite o ano em que você está: "))
idade = atual - nasc
meses = idade * 12
semanas = idade * 53
dias = idade * 365

print(f"Sua idade em anos é aproximadamente {idade}, sua idade em mêses é aproximadamente {meses}, sua idade em semanas é aproximadamente {semanas} e sua idade em dias é aproximadamente {dias}")