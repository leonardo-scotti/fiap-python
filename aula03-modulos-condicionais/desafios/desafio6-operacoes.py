def verificar_operacao(operacao):
    operacoes = ["+", "-", "*", "/"]

    if operacao in operacoes:
        return True
    else:
        return False


num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
operacao = input("Escolha a operação (+, -, * ou /): ")

if verificar_operacao(operacao):
    if operacao == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Digite uma operação válida (+, -, * ou /)!!!")