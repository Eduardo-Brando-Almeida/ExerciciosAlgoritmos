l1 = []
l2 = []
for i in range(10):
    x = int(input(f"L1 - Digite o {i+1}o. valor: "))
    l1.append(x)
print("L1 = ", l1)
for i in range(10):
    x = int(input(f"L2 - Digite o {i+1}o. valor: "))
    l2.append(x)
print("L2 = ", l2)

c1 = set(l1)
c2 = set(l2)
print("C1 = ", c1)
print("C2 = ", c2)

c = c1.union(c2)

print(c)