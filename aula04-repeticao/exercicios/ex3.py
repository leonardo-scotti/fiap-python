n = int(input("Digite um número para saber sua tabuada: "))

for i in range(26):
    produto = n * i
    print(f"{n} x {i}: {produto}")