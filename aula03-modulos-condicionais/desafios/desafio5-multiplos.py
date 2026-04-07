def multiplos(num1, num2):
    if num1 > num2:
        if num1 % num2 == 0:
            return True
        else:
            return False
    else:
        if num2 % num1 == 0:
            return True
        else:
            return False

a = int(input(f"Digite um número: "))
b = int(input(f"Digite outro número: "))

verificar = multiplos(a, b)

if verificar:
    print("São múltiplos")
else:
    print("Não são múltiplos")