import random

def validar_inteiro(number):
    while number <= 0:
        print("Digie um número inteiro maior que ZERO!")
        number = int(input("Digite novamente o número: "))

    return number

n = int(input("Digite um número inteiro: "))
n = validar_inteiro(n)

numbers = []

i = 0
while i < n:
    number = random.randint(1, 100)
    numbers.append(number)
    i += 1

print(numbers)