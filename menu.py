import estoque

continua = 1
while (continua == 1):
    try:
        escolha_str = input('ESTOQUE MERCADO\nEscolha sua opção:\n1-Cadastro\n2-Consulta\n3-Sair\n')
        escolha = int(escolha_str)
    except ValueError:
        print('Digite uma opção valida!')
    if escolha == 1:
        estoque.cadastro_prod()
        print('Produto cadastrado com sucesso!')
    elif escolha == 2:
        estoque.consulta_prod()
    elif escolha == 3:
        break
    else:
        print('Digite uma opção valida!')