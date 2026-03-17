print('======== CONVERSOR DE TEMPERATURA ========')
print('ESCOLHA PARA QUAL DESEJA CONVERTER:\n'
      '1 - CELSIUS\n'
      '2 - FAHRENHEIT\n'
      '3 - SAIR\n')

opcao = int(input('Escolha: '))

if opcao == 1 :
    print('Bora calcular os graus CELSIUS!!!')
    fahrenheit = float(input('Digite os graus FAHRENHEIT: '))

    calsius = (fahrenheit - 32) * (5 / 9)
elif opcao == 2:
    print('Bora calcular os graus FAHRENHEIT!!!')
    celsius = float(input('Digite os graus CELSIUS: '))

    fahrenheit = (celsius * (9 / 5)) + 32
else :
