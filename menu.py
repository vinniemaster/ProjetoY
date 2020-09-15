import estoque
import os

print("***Controle de estoque***")
continua = 1
while (continua == 1):
    try:
        escolha = int(input('\n1-Cadastro\n2-Consulta\n3-Sair\nEscolha sua opção:'))
    except ValueError:
        print('Digite uma opção valida!')
    if (escolha == 1):
        estoque.cadastro_prod()
        print('Produto cadastrado com sucesso!')
        input('Continue')
    elif (escolha == 2):
        estoque.consulta_prod()
        input('Continue')
    elif (escolha == 3):
        break
    else:
        print('Digite uma opção valida!')
        input('Continue')

    clear = lambda:os.system('clear')
    clear()