print('======== CONVERSOR DE TEMPERATURA ========')
fahrenheit = input('Digite os graus em fahrenheit: ')

celsius = (float(fahrenheit) - 32) * (5 / 9)

print(f'{fahrenheit} graus Fahrenheit são {celsius} graus Celsius!')