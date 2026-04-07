def maior_numero(number1, number2):
    if number1 == number2:
        print("Os números são iguais.")
    elif number1 > number2:
        print(f"O número: {number1} é maior que {number2}.")
    else:
        print(f"O número {number2} é maior que {number1}")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

maior_numero(numero1, numero2)