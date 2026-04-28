validar = "s"

while validar == "s":
    print("Olá, Mundo!")
    validar = input("Deseja repetir a mensagem? (s/n): ")

    while validar != "s" and validar != "n":
        print("Entrada errada! Digite 's' ou 'n'!")
        validar = input("Digite novamente (s/n):")

    if validar == "n":
        print("Fim")
        break