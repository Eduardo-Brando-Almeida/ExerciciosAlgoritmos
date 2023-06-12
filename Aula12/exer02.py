def primo(n):
    i = 1
    contador = 0
    while i <= n:
        if (n % i) == 0:
            contador += 1
        i += 1
    if contador == 2:
        return True
    else:
        return False


a = int(input("Dígite um número: "))
if primo(a):
    print(f"O numero {a} é primo")
else:
    print(f"O numero {a} NÃO é primo")
