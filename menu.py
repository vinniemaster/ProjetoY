import estoque

continua = 1
while (continua == 1):
    escolha_str = input('ESTOQUE MERCADO\nEscolha sua opção:\n1-Cadastro\n2-Consulta\n3-Sair\n')
    escolha = int(escolha_str)

    if escolha == 1:
        try:
            cadastro_prod()
        except (ValueError, RuntimeError, TypeError, NameError):
            print('Digite uma opção valida')
        pass
#     elif escolha == 2:
#         try:
# #           class/function()
#             print('Produto Cadastrado com sucesso')
#         except (RuntimeError, TypeError, NameError, OSError):
#             print('Sem produtos cadastrados')
#         pass
    elif escolha == 3:
        break
    else:
        print('opção inválida!')