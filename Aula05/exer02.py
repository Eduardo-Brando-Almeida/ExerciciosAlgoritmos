n1 = float(input("Entre com a primeira nota: "))
n2 = float(input("Entre com a segunda nota: "))
n3 = float(input("Entre com a terceira nota: "))
media = (n1 + n2 + n3) / 3
if media < 3.0:
    print(f"Sua média foi {media}. Reprovado!")
if media >= 3.0  < 7.0:
    print(f"Sua média foi {media}. Exame!")
    nota = 12 - media
    print(f"Você precisa tirar no mínimo {nota}")
if media >= 7.0 <= 10.0:
    print(f"Sua média foi {media}. Aprovado!!!🥳🎉")