from turtle import Tbuffer

from _testcapi import testBuf

from model import model_lead

def add_lead():
    name = input('Nome: ')
    email = input('Email: ')
    stage = input('Etapa no funil: ')

    print(model_lead(name,email,stage))

def main():
    while True:
        print('\nMini CRM de Leads')
        print('[1] Adicionar lead')
        print('[2] Listar lead')
        print('[0] Sair do programa')

        opt = input("Escolha uma opção:")

        if opt == '1':
            add_lead()
        elif opt == '2':
            print('\nListar leads')
        elif opt == '0':
            print('Até mais...')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    main()