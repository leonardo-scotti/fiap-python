cont = 1
valor = 0

while cont <= 5:
    atual = float(input("Digite um valor: "))

    if atual > valor:
        valor = atual

    cont += 1

print(f"O maior valor digitado foi: {valor}")