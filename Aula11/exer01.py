t = ()
for i in range(10):
    x = int(input(f"Digite o {i + 1}º número: "))
    t = t + (x,)

print(t[::-1])
